# config/db_router.py

from config.session_registry import SESSIONS

def get_session_class(db_type):
    return SESSIONS.get(db_type)

from sqlalchemy import create_engine
from config.db_config import build_url

def get_engine(db_type):
    url = build_url(db_type)
    return create_engine(url)