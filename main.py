from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from database import get_session, engine, Base
from models import Book, Review, User
from crud import get_books, get_book, create_book, update_book, delete_book, get_reviews, create_review, get_book_summary_and_rating, get_user_by_username, create_user, get_password_hash
from schemas import Book as BookSchema, BookCreate, BookUpdate, Review as ReviewSchema, ReviewCreate, UserCreate, UserInDB,BookSummary
import secrets
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
app = FastAPI()

security = HTTPBasic()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

async def authenticate(credentials: HTTPBasicCredentials = Depends(security), session: AsyncSession = Depends(get_session)):
    user = await get_user_by_username(session, credentials.username)
    if user and verify_password(credentials.password, user.hashed_password):
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Basic"},
    )

@app.post("/users/", response_model=UserInDB)
async def register_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username,email=user.email, hashed_password=hashed_password)
    return await create_user(session, db_user)

@app.post("/books", response_model=BookSchema)
async def add_book(book: BookCreate, session: AsyncSession = Depends(get_session), user: User = Depends(authenticate)):
    new_book = await create_book(session, Book(**book.dict()))
    return new_book

@app.get("/books", response_model=List[BookSchema])
async def read_books(session: AsyncSession = Depends(get_session), user: User = Depends(authenticate)):
    books = await get_books(session)
    return books

@app.get("/books/{book_id}", response_model=BookSchema)
async def read_book(book_id: int, session: AsyncSession = Depends(get_session), user: User = Depends(authenticate)):
    book = await get_book(session, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}", response_model=BookSchema)
async def update_book_info(book_id: int, book: BookUpdate, session: AsyncSession = Depends(get_session), user: User = Depends(authenticate)):
    updated_book = await update_book(session, book_id, book.dict(exclude_unset=True))
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@app.delete("/books/{book_id}", response_model=BookSchema)
async def delete_book_info(book_id: int, session: AsyncSession = Depends(get_session), user: User = Depends(authenticate)):
    deleted_book = await delete_book(session, book_id)
    if not deleted_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return deleted_book

@app.post("/books/{book_id}/reviews", response_model=ReviewSchema)
async def add_review(book_id: int, review: ReviewCreate, session: AsyncSession = Depends(get_session), user: User = Depends(authenticate)):
    new_review = await create_review(session, Review(book_id=book_id, **review.dict()))
    return new_review

@app.get("/books/{book_id}/reviews", response_model=List[ReviewSchema])
async def read_reviews(book_id: int, session: AsyncSession = Depends(get_session), user: User = Depends(authenticate)):
    reviews = await get_reviews(session, book_id)
    return reviews

@app.get("/books/{book_id}/summary", response_model=BookSummary)
async def read_book_summary(book_id: int, session: AsyncSession = Depends(get_session), user: User = Depends(authenticate)):
    summary, avg_rating, review_count = await get_book_summary_and_rating(session, book_id)
    if summary is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"summary": summary, "avg_rating": avg_rating, "review_count": review_count}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
