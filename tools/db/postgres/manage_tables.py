import sys
import os
import logging

# Add the project folder to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from myapp import create_app
from models.models_definitions import db
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()  

def is_production_environment() -> bool:
    """
    Check if the current environment is production.

    Returns:
        bool: True if the environment is production, False otherwise.
    """
    return os.getenv("FLASK_ENV") == "production"

def prompt_user_choice() -> str:
    """
    Prompt the user to select a database operation option.

    Returns:
        str: The user's choice ('1' or '2').
    """
    print("WARNING: This script modifies database tables.")
    print("Choose one of the following options:")
    print("1. Drop all tables and recreate them (WARNING: All data will be lost!)")
    print("2. Create missing tables only (safe)")
    return input("Enter your choice (1 or 2): ").strip()

def handle_database_operations(choice: str):
    """
    Execute database operations based on the user's choice.

    Args:
        choice (str): User's selected operation ('1' or '2').
    """
    app = create_app()
    with app.app_context():
        if choice == "1":
            confirm = input("Are you sure? This will erase ALL data. (y/n): ")
            if confirm.lower() != "y":
                logging.info("Operation cancelled.")
                return
            db.drop_all()
            db.create_all()
            logging.info("All tables have been dropped and recreated.")
        elif choice == "2":
            db.create_all()
            logging.info("Missing tables have been created.")
        else:
            logging.warning("Invalid option. No operation was performed.")

def main():
    """
    Main function to run the database management script.
    """
    if is_production_environment():
        logging.error("This script cannot be run in a production environment.")
        sys.exit(1)

    choice = prompt_user_choice()
    handle_database_operations(choice)

if __name__ == "__main__":
    main()
