from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from dotenv import load_dotenv
import os 
from sqlalchemy.orm import declarative_base
from typing import AsyncGenerator

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("Unable to fetch the database url")


Base = declarative_base()

engine = create_async_engine(
    DATABASE_URL,
    echo=True
)

LocalAsyncSession = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with LocalAsyncSession() as db:
        yield db