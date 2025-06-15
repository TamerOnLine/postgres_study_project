from config.session_registry import SESSIONS

def get_credentials(db_type=None):
    ...
    SessionClass = SESSIONS.get(db_type)
