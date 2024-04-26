from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase



sync_engine = create_engine(
    url="postgresql+psycopg://postgres:postgres@localhost:5432/db_bot",
    echo=True,
    pool_size=5,
    max_overflow=10
)

Session_factory = sessionmaker(bind=sync_engine, autocommit=False, autoflush=False)

class Base(DeclarativeBase):
    pass