from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

MYSQLHOST = os.getenv("MYSQLHOST", "localhost")
MYSQLUSER = os.getenv("MYSQLUSER", "root")
MYSQLPASSWORD = os.getenv("MYSQLPASSWORD", "")
MYSQLPORT = os.getenv("MYSQLPORT", "3306")
MYSQLDATABASE = os.getenv("MYSQLDATABASE", "proyecto")

DB_URL = f"mysql+pymysql://{MYSQLUSER}:{MYSQLPASSWORD}@{MYSQLHOST}:{MYSQLPORT}/{MYSQLDATABASE}"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()