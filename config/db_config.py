import os
from dotenv import load_dotenv

load_dotenv()

def get_database_credentials():
    return {
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "host": os.getenv("DB_HOST", "localhost"),
        "port": os.getenv("DB_PORT", 5432),
        "dbname": os.getenv("DB_NAME")
    }
