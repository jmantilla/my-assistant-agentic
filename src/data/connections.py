from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database connection settings
DATABASE_URL = "sqlite:///my_database.db"  # Example for SQLite, change as needed

# Create a new database engine instance
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session instance
session = Session()

def get_session():
    """Returns a new session instance."""
    return Session()

def close_session(session):
    """Closes the provided session."""
    session.close()