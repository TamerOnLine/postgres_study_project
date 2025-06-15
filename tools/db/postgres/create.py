try:
    import setup_path  # يضيف مسار الجذر عند التشغيل المباشر
except ImportError:
    import os, sys
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from config.postgres_config import engine, Base, get_database_credentials

description = "Create PostgreSQL database (if missing) and initialize all tables"

def create_database_if_not_exists():
    creds = get_database_credentials()
    dbname = creds["dbname"]
    user = creds["user"]
    password = creds["password"]
    host = creds["host"]
    port = creds["port"]

    try:
        conn = psycopg2.connect(
            dbname='postgres', user=user, password=password, host=host, port=port
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (dbname,))
        exists = cursor.fetchone()

        if not exists:
            cursor.execute(f'CREATE DATABASE "{dbname}"')
            print(f"✅ Created database: {dbname}")
        else:
            print(f"ℹ️ Database '{dbname}' already exists.")

        cursor.close()
        conn.close()

    except Exception as e:
        print("❌ Error creating database:", e)

def create_all_tables():
    print("✅ Creating all tables...")
    Base.metadata.create_all(bind=engine)
    print("🎉 Done.")

def run():
    create_database_if_not_exists()
    create_all_tables()

if __name__ == "__main__":
    run()
