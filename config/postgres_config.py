# config/postgres_config.py

def get_postgres_url_from_credentials(creds):
    return (
        f"postgresql+psycopg2://{creds['user']}:{creds['password']}"
        f"@{creds['host']}:{creds['port']}/{creds['dbname']}"
    )
