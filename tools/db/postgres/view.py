# tools/db/postgres/view.py

try:
    import setup_path  # لتفعيل مسار المشروع عند التشغيل المباشر
except ImportError:
    import os, sys
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)

import os
from sqlalchemy import create_engine, text, inspect
from config.postgres_config import engine

def list_tables():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    return tables

def view_table_content(table_name, limit=5):
    try:
        with engine.connect() as conn:
            result = conn.execute(text(f"SELECT * FROM {table_name} LIMIT :limit"), {"limit": limit})
            rows = result.fetchall()
            columns = result.keys()

            if not rows:
                print(f"ℹ️ Table '{table_name}' is empty.")
                return

            print(f"\n📊 Preview of '{table_name}' (max {limit} rows):")
            print("-" * 60)
            print(" | ".join(columns))
            print("-" * 60)
            for row in rows:
                print(" | ".join(str(val) for val in row))
            print("-" * 60)
    except Exception as e:
        print(f"❌ Error reading table '{table_name}': {e}")

def run():
    print("\n📂 Fetching list of tables...")
    tables = list_tables()
    if not tables:
        print("⚠️ No tables found in the database.")
        return

    print("\n📋 Available Tables:")
    for idx, table in enumerate(tables, 1):
        print(f"{idx}. {table}")
    print("0. Cancel")

    try:
        choice = int(input("Select a table number to view: ").strip())
    except ValueError:
        print("❌ Invalid input.")
        return

    if choice == 0:
        print("❎ Operation cancelled.")
        return
    elif 1 <= choice <= len(tables):
        selected = tables[choice - 1]
        view_table_content(selected)
    else:
        print("❌ Invalid table number.")
