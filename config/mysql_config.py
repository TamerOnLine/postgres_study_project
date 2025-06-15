try:
    from config.db_credentials import get_credentials
except ImportError:
    from .db_credentials import get_credentials

def get_mysql_url():
    creds = get_credentials("mysql")
    return f"mysql+pymysql://{creds['user']}:{creds['password']}@{creds['host']}:{creds['port']}/{creds['dbname']}"
