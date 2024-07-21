# crud.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from models import Book, User, Review
from sqlalchemy import func
from models import User
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

async def get_user_by_username(session: AsyncSession, username: str):
    result = await session.execute(select(User).where(User.username == username))
    return result.scalars().first()

async def create_user(session: AsyncSession, user: User):
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


# Book CRUD operations
async def get_books(session: AsyncSession):
    result = await session.execute(select(Book).options(joinedload(Book.reviews)))
    return result.scalars().unique().all()

async def get_book(session: AsyncSession, book_id: int):
    result = await session.execute(select(Book).where(Book.id == book_id).options(joinedload(Book.reviews)))
    return result.scalar()

async def create_book(session: AsyncSession, book: Book):
    session.add(book)
    await session.commit()
    await session.refresh(book)
    return book

async def update_book(session: AsyncSession, book_id: int, book_update: dict):
    result = await session.execute(select(Book).where(Book.id == book_id))
    book = result.scalar()
    if book:
        for key, value in book_update.items():
            setattr(book, key, value)
        await session.commit()
        await session.refresh(book)
    return book

async def delete_book(session: AsyncSession, book_id: int):
    result = await session.execute(select(Book).where(Book.id == book_id))
    book = result.scalar()
    if book:
        await session.delete(book)
        await session.commit()
    return book

# Review CRUD operations
async def get_reviews(session: AsyncSession, book_id: int):
    result = await session.execute(select(Review).where(Review.book_id == book_id).options(joinedload(Review.user)))
    return result.scalars().unique().all()

async def create_review(session: AsyncSession, review: Review):
    session.add(review)
    await session.commit()
    await session.refresh(review)
    return review

async def get_book_summary_and_rating(session: AsyncSession, book_id: int):
    book_result = await session.execute(
        select(Book)
        .where(Book.id == book_id)
    )
    book = book_result.scalar()

    if not book:
        return None, None, None

    review_result = await session.execute(
        select(
            func.avg(Review.rating).label('avg_rating'),
            func.count(Review.id).label('review_count')
        )
        .where(Review.book_id == book_id)
    )
    review_summary = review_result.one()
    avg_rating = review_summary.avg_rating or 0
    review_count = review_summary.review_count or 0

    return book.summary, avg_rating, review_count