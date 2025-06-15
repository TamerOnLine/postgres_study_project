# config/credentials_helper.py

import os
from dotenv import load_dotenv
load_dotenv()

def get_credentials_from_env(db_type: str):
    if db_type == "postgres":
        return {
            "user": os.getenv("POSTGRES_DB_USER"),
            "password": os.getenv("POSTGRES_DB_PASSWORD"),
            "host": os.getenv("POSTGRES_DB_HOST"),
            "port": os.getenv("POSTGRES_DB_PORT"),
            "dbname": os.getenv("POSTGRES_DB_NAME"),
        }
    elif db_type == "mysql":
        return {
            "user": os.getenv("MYSQL_DB_USER"),
            "password": os.getenv("MYSQL_DB_PASSWORD"),
            "host": os.getenv("MYSQL_DB_HOST"),
            "port": os.getenv("MYSQL_DB_PORT"),
            "dbname": os.getenv("MYSQL_DB_NAME"),
        }
    elif db_type == "sqlite":
        return {
            "path": os.getenv("SQLITE_DB_NAME", "default.db"),
        }
    else:
        raise ValueError(f"Unsupported DB type: {db_type}")
