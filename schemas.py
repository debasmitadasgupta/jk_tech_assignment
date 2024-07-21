# schemas.py
from pydantic import BaseModel
from typing import List, Optional

class ReviewBase(BaseModel):
    review_text: str
    rating: int

class ReviewCreate(ReviewBase):
    user_id: int

class Review(ReviewBase):
    id: int
    book_id: int
    user_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    hashed_password: str

class User(UserBase):
    id: int
    reviews: List[Review] = []

    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    genre: Optional[str] = None
    year_published: Optional[int] = None
    summary: Optional[str] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True

class BookSummary(BaseModel):
    summary: str
    avg_rating: float
    review_count: int