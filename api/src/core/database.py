import os
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncAttrs
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Text, JSON, DateTime
from api.src.core.config import settings  # Adjust the import path
import datetime

Base = declarative_base(cls=AsyncAttrs)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    password_hash = Column(String(128))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class Conversation(Base):
    __tablename__ = "conversations"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    messages = Column(JSON)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class KnowledgeEntry(Base):
    __tablename__ = "knowledge_base"
    id = Column(Integer, primary_key=True)
    content = Column(Text)
    embedding = Column(JSON)
    scope = Column(String(20))
    source = Column(String(50))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


# Get DATABASE_URL from settings
DATABASE_URL = settings.database_url

engine = create_async_engine(
    DATABASE_URL, pool_size=20, max_overflow=10, pool_pre_ping=True
)

AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    import sys

    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(init_db())
