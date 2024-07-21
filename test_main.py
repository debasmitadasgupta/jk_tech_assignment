import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from main import app, get_session
from database import Base
from models import User, Book
from passlib.context import CryptContext

# Setup database and test client
DATABASE_URL = "postgresql+asyncpg://postgres:root@localhost/assignment"
engine = create_async_engine(DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Initialize the CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@pytest.fixture(scope="module")
async def db():
    async_session = TestingSessionLocal()
    yield async_session
    await async_session.close()

@pytest.fixture(scope="module")
def test_client():
    app.dependency_overrides[get_session] = override_get_session
    with TestClient(app) as client:
        yield client

async def override_get_session():
    async_session = TestingSessionLocal()
    try:
        yield async_session
    finally:
        await async_session.close()



# # Test case for registering a user
def test_register_user(test_client):
    response = test_client.post("/users/", json={"username": "newuser", "email": "newuser@example.com", "password": "newpassword123"})
    assert response.status_code == 200
    assert response.json()["username"] == "newuser"
    assert response.json()["email"] == "newuser@example.com"

# Test case for authenticating a user and adding a book
def test_authenticate_user_and_add_book(test_client):
    response = test_client.post(
        "/books",
        json={"title": "New Book", "author": "Author", "genre": "Fiction", "year_published": 2022, "summary": "Summary of the new book"},
        auth=("newuser", "newpassword123")
    )
    assert response.status_code == 200
    assert response.json()["title"] == "New Book"
    assert response.json()["author"] == "Author"

def test_read_books(test_client):
    response = test_client.get("/books", auth=("newuser", "newpassword123"))
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_book(test_client):
    response = test_client.get("/books/1", auth=("newuser", "newpassword123"))
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Book"

def test_update_book(test_client):
    response = test_client.put("/books/2", json={"title": "Updated Book"},auth=("newuser", "newpassword123"))
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Book"


def test_add_review(test_client):
    response = test_client.post(
        "/books/1/reviews",
        json={"review_text": "Great book!", "rating": 5, "user_id": 1, "book_id": 1},
        auth=("newuser", "newpassword123")
    )
    assert response.status_code == 200
    assert response.json()["review_text"] == "Great book!"

def test_read_reviews(test_client):
    response = test_client.get("/books/1/reviews", auth=("newuser", "newpassword123"))
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_book_summary(test_client):
    response = test_client.get("/books/1/summary", auth=("newuser", "newpassword123"))
    assert response.status_code == 200
    assert "summary" in response.json()
