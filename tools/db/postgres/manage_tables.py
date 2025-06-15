# tools/db/postgres/manage_tables.py

try:
    import setup_path
except ImportError:
    import os, sys
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)

import sys
import os
import logging
from dotenv import load_dotenv

from config.postgres_config import engine, Base

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

def is_production_environment() -> bool:
    return os.getenv("FLASK_ENV") == "production"

def prompt_user_choice() -> str:
    print("\n⚠️ WARNING: This will modify database tables.")
    print("Choose one of the following options:")
    print("1. 🗑️ Drop ALL tables and recreate them (DANGER: all data will be LOST!)")
    print("2. ✅ Create only missing tables (safe)")
    return input("Enter your choice (1 or 2): ").strip()

def handle_database_operations(choice: str):
    if choice == "1":
        confirm = input("⚠️ Are you sure? This will ERASE ALL data. (y/n): ").strip().lower()
        if confirm != "y":
            logging.info("❎ Operation cancelled.")
            return
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        logging.info("🗑️ All tables dropped and recreated.")
    elif choice == "2":
        Base.metadata.create_all(bind=engine)
        logging.info("✅ Missing tables created.")
    else:
        logging.warning("❌ Invalid option. No operation performed.")

def run():
    if is_production_environment():
        logging.error("❌ This script cannot be run in production.")
        sys.exit(1)

    choice = prompt_user_choice()
    handle_database_operations(choice)

if __name__ == "__main__":
    run()
