"""
database.py — NO-DATABASE MODE
Uses real SQLAlchemy Base so model class definitions work,
but NO engine or session is created. Everything runs in-memory/mock.
"""
from sqlalchemy.ext.declarative import declarative_base
<<<<<<< HEAD
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
=======
from sqlalchemy.orm import Session
from typing import Optional
>>>>>>> 88626cf847d9b741e7b52fc7c823bf3a4851605c

# Real Base so model classes (User, Image, etc.) can be defined normally
Base = declarative_base()

# No engine, no session — all None
engine = None
SessionLocal = None
DB_AVAILABLE = False


def get_db():
    """Dependency — always yields None (no DB mode)."""
    yield None
