from base_tool_template import run_tool_template
from config.postgres_config import get_database_credentials
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def run():
    db_config = get_database_credentials()
    db_name = db_config["database"]

    try:
        connection = psycopg2.connect(
            user=db_config["user"],
            password=db_config["password"],
            host=db_config["host"],
            port=db_config["port"],
        )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE {db_name};")
        print(f"✅ Database '{db_name}' created successfully.")
        cursor.close()
        connection.close()
    except psycopg2.errors.DuplicateDatabase:
        print(f"⚠️ Database '{db_name}' already exists.")
    except Exception as e:
        print(f"❌ Error creating database: {e}")

if __name__ == "__main__":
    run_tool_template(run, "Create PostgreSQL Database")
