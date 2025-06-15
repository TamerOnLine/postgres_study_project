import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

load_dotenv()

def build_url(engine):
    if engine == "sqlite":
        db_name = os.getenv("SQLITE_DB_NAME", "default.db")
        return f"sqlite:///{db_name}"
    elif engine == "postgres":
        return (
            f"postgresql+psycopg2://{os.getenv('POSTGRES_DB_USER')}:{os.getenv('POSTGRES_DB_PASSWORD')}"
            f"@{os.getenv('POSTGRES_DB_HOST')}:{os.getenv('POSTGRES_DB_PORT')}/{os.getenv('POSTGRES_DB_NAME')}"
        )
    elif engine == "mysql":
        return (
            f"mysql+pymysql://{os.getenv('MYSQL_DB_USER')}:{os.getenv('MYSQL_DB_PASSWORD')}"
            f"@{os.getenv('MYSQL_DB_HOST')}:{os.getenv('MYSQL_DB_PORT')}/{os.getenv('MYSQL_DB_NAME')}"
        )
    else:
        raise ValueError(f"Unsupported engine: {engine}")

def test_connection(name, url):
    print(f"\n🔌 Testing connection to [{name}] → {url}")
    try:
        engine = create_engine(url)
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print(f"✅ Connection successful: {result.scalar()}")
    except SQLAlchemyError as e:
        print(f"❌ Connection failed: {e}")

def test_all_connections():
    engines = {
        "SQLite": "sqlite",
        "PostgreSQL": "postgres",
        "MySQL": "mysql",
    }

    for name, eng in engines.items():
        try:
            url = build_url(eng)
            test_connection(name, url)
        except Exception as e:
            print(f"⚠️ Skipped {name}: {e}")

if __name__ == "__main__":
    print("\n🔍 Testing all database connections...\n")
    test_all_connections()
    print("\n✅ Done testing connections.\n")
