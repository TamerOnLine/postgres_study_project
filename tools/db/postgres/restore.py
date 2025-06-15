# tools/db/postgres/restore.py

try:
    import setup_path  # لإضافة مسار المشروع عند التشغيل المباشر
except ImportError:
    import os, sys
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)

import os
import subprocess
from config.db_config import get_database_credentials

PSQL_PATHS = [
    r"C:\\Program Files\\PostgreSQL\\17\\bin\\psql.exe",
    r"C:\\Program Files\\PostgreSQL\\15\\bin\\psql.exe",
    r"C:\\Program Files\\PostgreSQL\\14\\bin\\psql.exe",
    "psql"  # fallback في حال كان psql في PATH
]

def find_psql():
    for path in PSQL_PATHS:
        if os.path.exists(path):
            return path
    raise FileNotFoundError("❌ psql not found in known locations or PATH.")

def choose_backup_file(folder="./backups"):
    files = [f for f in os.listdir(folder) if f.endswith(".sql")]
    if not files:
        raise FileNotFoundError("❌ No .sql backup files found in the 'backups' folder.")

    print("\n📂 Available backup files:")
    for idx, file in enumerate(files):
        print(f"{idx + 1}. {file}")

    while True:
        try:
            choice = int(input("Select file number to restore: "))
            if 1 <= choice <= len(files):
                return os.path.join(folder, files[choice - 1])
            print("❌ Invalid number.")
        except ValueError:
            print("❌ Enter a valid integer.")

def restore_backup():
    creds = get_database_credentials()
    psql_path = find_psql()
    backup_file = choose_backup_file()

    os.environ["PGPASSWORD"] = creds["password"]

    restore_command = [
        psql_path,
        "-h", creds["host"],
        "-p", str(creds["port"]),
        "-U", creds["user"],
        "-d", creds["dbname"],
        "-f", backup_file
    ]

    try:
        print(f"\n🔁 Restoring from: {backup_file}")
        subprocess.run(restore_command, check=True)
        print("✅ Database restored successfully.")
    except subprocess.CalledProcessError as e:
        print("❌ Error during restoration:", e)
    except FileNotFoundError as e:
        print(e)

def run():
    restore_backup()

if __name__ == "__main__":
    run()
