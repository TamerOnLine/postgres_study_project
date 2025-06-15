try:
    from config.db_credentials import get_credentials
except ImportError:
    from .db_credentials import get_credentials

def get_postgres_url():
    creds = get_credentials("postgres")
    return f"postgresql+psycopg2://{creds['user']}:{creds['password']}@{creds['host']}:{creds['port']}/{creds['dbname']}"

