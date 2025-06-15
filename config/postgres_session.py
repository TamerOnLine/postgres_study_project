# config/postgres_session.py

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config.credentials_helper import get_credentials_from_env
from config.postgres_config import get_postgres_url_from_credentials

creds = get_credentials_from_env("postgres")
engine = create_engine(get_postgres_url_from_credentials(creds))
PostgresSession = sessionmaker(bind=engine)
