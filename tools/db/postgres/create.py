# tools/db/postgres/create.py

import os
import sys

# 🧭 إعداد المسار الجذري للمشروع
CURRENT = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(CURRENT, "../../../"))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from base_tool_template import run_tool_template
from config.credentials_helper import get_credentials_from_env

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def perform_create():
    creds = get_credentials_from_env("postgres")
    db_name = creds["dbname"]

    try:
        connection = psycopg2.connect(
            user=creds["user"],
            password=creds["password"],
            host=creds["host"],
            port=creds["port"],
        )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE {db_name};")
        print(f"✅ Database '{db_name}' created successfully.")
        cursor.close()
        connection.close()
    except psycopg2.errors.DuplicateDatabase:
        print(f"⚠️ Database '{db_name}' already exists.")
    except Exception as e:
        print(f"❌ Error creating database: {e}")

def run():
    run_tool_template(perform_create, "Create PostgreSQL Database")

if __name__ == "__main__":
    run()
