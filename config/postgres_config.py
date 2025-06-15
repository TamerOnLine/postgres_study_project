try:

    from config.db_config import get_database_credentials
except ImportError:
    
    from .db_config  import get_database_credentials

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

creds = get_database_credentials()

DATABASE_URL = f"postgresql://{creds['user']}:{creds['password']}@{creds['host']}:{creds['port']}/{creds['dbname']}"
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
