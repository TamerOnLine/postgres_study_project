# tools/db/postgres/drop_table.py

import os
import sys
from sqlalchemy import MetaData
from sqlalchemy.exc import SQLAlchemyError

# 🧭 إعداد المسار الجذري للمشروع
CURRENT = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(CURRENT, "../../../"))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from config.postgres_config import engine, Base
from base_tool_template import run_tool_template

def perform_drop_table():
    metadata = MetaData()
    metadata.reflect(bind=engine)

    tables = list(metadata.tables.keys())
    if not tables:
        print("ℹ️ No tables found in the database.")
        return

    print("📋 Existing tables:")
    for i, table_name in enumerate(tables, start=1):
        print(f"{i}. {table_name}")
    print("0. Drop ALL tables")
    print("-1. Cancel")

    try:
        choice = int(input("Select table number to drop: ").strip())
    except ValueError:
        print("❌ Invalid input.")
        return

    if choice == -1:
        print("❎ Operation cancelled.")
    elif choice == 0:
        confirm = input("⚠️ Are you sure you want to DROP ALL tables? (yes/no): ").lower()
        if confirm == "yes":
            try:
                Base.metadata.drop_all(bind=engine)
                print("🗑️ All tables dropped successfully.")
            except SQLAlchemyError as e:
                print("❌ Error dropping all tables:", e)
        else:
            print("❎ Operation cancelled.")
    elif 1 <= choice <= len(tables):
        table_name = tables[choice - 1]
        try:
            table = metadata.tables[table_name]
            table.drop(bind=engine)
            print(f"🗑️ Table '{table_name}' dropped successfully.")
        except SQLAlchemyError as e:
            print(f"❌ Error dropping table '{table_name}':", e)
    else:
        print("❌ Invalid choice.")

def run():
    run_tool_template(perform_drop_table, "Drop Table from PostgreSQL Database")

if __name__ == "__main__":
    run()
