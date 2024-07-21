# database.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+asyncpg://postgres:root@localhost/assignment"

# Create an asynchronous engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create a configured "Session" class
async_session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# Create a Base class for the declarative base
Base = declarative_base()

# Dependency to get a session for each request
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session