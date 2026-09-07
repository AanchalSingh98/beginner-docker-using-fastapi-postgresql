import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:password@localhost:5432/fastapi_db"
)

engine = create_engine(db_url)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)