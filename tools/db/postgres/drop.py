try:
    import setup_path  # يضيف مسار الجذر عند التشغيل المباشر
except ImportError:
    import os, sys
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from config.postgres_config import get_database_credentials

description = "Drop PostgreSQL database if it exists"

def drop_database_if_exists():
    creds = get_database_credentials()
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
    run()
