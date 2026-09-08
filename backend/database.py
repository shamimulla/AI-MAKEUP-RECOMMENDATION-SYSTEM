from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Use database URL from environment, or default to zero-config local SQLite
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./glowmatchai.db")

connect_args = {"check_same_thread": False} if SQLALCHEMY_DATABASE_URL.startswith("sqlite") else {}

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)
    if not SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
        with engine.connect():
            pass
except Exception as e:
    print(f"INFO: Database connection failed ({e}). Falling back to local SQLite database.")
    SQLALCHEMY_DATABASE_URL = "sqlite:///./glowmatchai.db"
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
