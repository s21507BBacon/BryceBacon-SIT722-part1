from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings

print(f"DATABASE_URL: {settings.DATABASE_URL}")  # For debugging

# SQLAlchemy database engine and session
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()