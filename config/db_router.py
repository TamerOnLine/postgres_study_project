# config/db_router.py

from config.session_registry import SESSIONS

def get_session_class(db_type):
    return SESSIONS.get(db_type)
