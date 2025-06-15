# config/test_connections.py

from config.db_router import get_engine

def test_all_connections():
    engines = {
        "SQLite": "sqlite",
        "PostgreSQL": "postgres",
        "MySQL": "mysql",
    }

    for name, key in engines.items():
        try:
            engine = get_engine(key)
            with engine.connect() as conn:
                result = conn.execute("SELECT 1")
                print(f"✅ {name} connection successful: {result.scalar()}")
        except Exception as e:
            print(f"❌ {name} connection failed: {e}")
