# tools/db/postgres/backup.py

try:
    import setup_path
except ImportError:
    import os, sys
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)

import os
import subprocess
from datetime import datetime
from config.db_config import get_database_credentials

COMMON_PG_DUMP_PATHS = [
    r"C:\\Program Files\\PostgreSQL\\17\\bin\\pg_dump.exe",
    r"C:\\Program Files\\PostgreSQL\\15\\bin\\pg_dump.exe",
    r"C:\\Program Files\\PostgreSQL\\14\\bin\\pg_dump.exe",
    r"C:\\Program Files\\PostgreSQL\\13\\bin\\pg_dump.exe",
    r"C:\\Program Files\\PostgreSQL\\12\\bin\\pg_dump.exe"
]

def find_pg_dump():
    for path in COMMON_PG_DUMP_PATHS:
        if os.path.exists(path):
            return path
    return "pg_dump"

def create_backup():
    pg_dump_path = find_pg_dump()
    creds = get_database_credentials()

    # إنشاء مجلد النسخ
    backup_folder = "./backups"
    os.makedirs(backup_folder, exist_ok=True)

    # سؤال المستخدم
    print("\n🔧 Do you want to set a custom backup filename?")
    print("➡ Leave empty to use the default (timestamped) name.")
    custom_name = input("Enter filename (without extension): ").strip()

    if custom_name:
        backup_filename = f"{custom_name}.sql"
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_filename = f"{creds['dbname']}_backup_{timestamp}.sql"

    backup_path = os.path.join(backup_folder, backup_filename)

    os.environ["PGPASSWORD"] = creds['password']

    dump_command = [
        pg_dump_path,
        "-h", creds['host'],
        "-p", str(creds['port']),
        "-U", creds['user'],
        "-d", creds['dbname'],
        "-f", backup_path
    ]

    try:
        print(f"\n📦 Starting backup for database '{creds['dbname']}'...")
        subprocess.run(dump_command, check=True)
        print(f"✅ Backup saved to: {backup_path}")
    except subprocess.CalledProcessError as e:
        print("❌ Backup failed (process error):", e)
    except FileNotFoundError:
        print("❌ pg_dump not found. Make sure it's installed or added to PATH.")

def run():
    create_backup()

if __name__ == "__main__":
    run()
