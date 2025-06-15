# tools/db/postgres/view.py

import os
import sys
from sqlalchemy import text, inspect

# 🧭 إعداد المسار الجذري للمشروع
CURRENT = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(CURRENT, "../../../"))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from config.postgres_session import engine
from base_tool_template import run_tool_template

def list_tables():
    inspector = inspect(engine)
    return inspector.get_table_names()

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

def perform_view_table():
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
    elif 1 <= choice <= len(tables):
        selected = tables[choice - 1]
        view_table_content(selected)
    else:
        print("❌ Invalid table number.")

def run():
    run_tool_template(perform_view_table, "View Table Content")

if __name__ == "__main__":
    run()
