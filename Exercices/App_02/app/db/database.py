from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

SQLALCHEMY_DATABASE_URL = os.getenv("DB_DATABASE_URL")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL 
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()