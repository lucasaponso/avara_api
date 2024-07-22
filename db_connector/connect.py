from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_PASSWORD = "RYy3GziqsVPPeP7abMzHZfSDj7DDKAX4vVMMfo"
DB_DATABASE = "library"
DB_USER = "root"
PORT_NUMBER = "3306"
HOST = "172.236.33.198"


URL_DATABASE = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{HOST}:{PORT_NUMBER}/{DB_DATABASE}'
engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



"""
Creates a new database session for each request.

Yields:
- Session: A SQLAlchemy session object for database operations.

Usage:
```
db = get_db()
try:
    # Perform database operations using the session
finally:
    # Close the session after database operations are done
    db.close()
```
"""

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()