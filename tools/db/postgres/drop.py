# tools/db/postgres/drop.py

import os
import sys

# ✅ أضف المسار الجذر للمشروع
CURRENT = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(CURRENT, "../../../"))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from base_tool_template import run_tool_template
from config.credentials_helper import get_credentials_from_env

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

description = "Drop PostgreSQL database if it exists"

def drop_database_if_exists():
    creds = get_credentials_from_env("postgres")
    dbname = creds["dbname"]
    user = creds["user"]
    password = creds["password"]
    host = creds["host"]
    port = creds["port"]

    try:
        conn = psycopg2.connect(
            dbname="postgres", user=user, password=password, host=host, port=port
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        # التحقق من وجود القاعدة
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (dbname,))
        exists = cursor.fetchone()

        if not exists:
            print(f"ℹ️ Database '{dbname}' does not exist.")
        else:
            # إنهاء كل الجلسات المتصلة
            cursor.execute("""
                SELECT pg_terminate_backend(pid)
                FROM pg_stat_activity
                WHERE datname = %s AND pid <> pg_backend_pid()
            """, (dbname,))
            print(f"🛑 Terminated other connections to '{dbname}'.")

            # حذف القاعدة
            cursor.execute(f'DROP DATABASE "{dbname}"')
            print(f"🗑️ Dropped database: {dbname}")

        cursor.close()
        conn.close()

    except Exception as e:
        print("❌ Error dropping database:", e)

def run():
    drop_database_if_exists()

if __name__ == "__main__":
    run_tool_template(run, "Drop PostgreSQL Database")

