try:
    import setup_path  # لتفعيل مسار الجذر عند التشغيل من ملفات فرعية
except ImportError:
    import os
    import sys
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if ROOT not in sys.path:
        sys.path.append(ROOT)

from config.postgres_config import engine, Base
from sqlalchemy import MetaData
from sqlalchemy.exc import SQLAlchemyError

description = "Drop a specific table or all tables from the PostgreSQL database"

def drop_tables():
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
        return
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
        return
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
    drop_tables()

if __name__ == "__main__":
    run()
