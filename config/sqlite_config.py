try:
    from config.db_credentials import get_credentials
except ImportError:
    from .db_credentials import get_credentials

def get_sqlite_url():
    creds = get_credentials("sqlite")
    return f"sqlite:///{creds['path']}"
