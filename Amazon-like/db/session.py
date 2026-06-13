from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql+asyncpg://postgres:root@localhost/amazon_db"
SYNC_DATABASE_URL = "postgresql://postgres:root@localhost/amazon_db"
async_engine = create_async_engine(DATABASE_URL)
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
)
Base = declarative_base()
