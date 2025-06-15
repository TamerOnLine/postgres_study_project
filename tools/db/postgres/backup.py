# tools/db/postgres/backup.py

import os
import sys

# 🧭 إعداد المسار الجذر للمشروع
CURRENT = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(CURRENT, "../../../"))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from base_tool_template import run_tool_template
from config.credentials_helper import get_credentials_from_env

import subprocess
from datetime import datetime
import getpass

# 🔍 مسارات pg_dump الشائعة (ويندوز + fallback)
COMMON_PG_DUMP_PATHS = [
    r"C:\Program Files\PostgreSQL\17\bin\pg_dump.exe",
    r"C:\Program Files\PostgreSQL\15\bin\pg_dump.exe",
    r"C:\Program Files\PostgreSQL\14\bin\pg_dump.exe",
    r"C:\Program Files\PostgreSQL\13\bin\pg_dump.exe",
    r"C:\Program Files\PostgreSQL\12\bin\pg_dump.exe",
    "pg_dump"
]

def find_pg_dump():
    for path in COMMON_PG_DUMP_PATHS:
        if os.path.exists(path):
            return path
    return "pg_dump"

def perform_backup():
    pg_dump_path = find_pg_dump()
    creds = get_credentials_from_env("postgres")

    now = datetime.now()
    backup_folder = os.path.join("backups", now.strftime("%Y"), now.strftime("%m"))
    os.makedirs(backup_folder, exist_ok=True)

    print("\n🔧 Do you want to set a custom backup filename?")
    print("➡ Leave empty to use the default (timestamped) name.")
    custom_name = input("Enter filename (without extension): ").strip()

    if custom_name:
        backup_filename = f"{custom_name}.sql"
    else:
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        backup_filename = f"{creds['dbname']}_backup_{timestamp}.sql"

    backup_path = os.path.join(backup_folder, backup_filename)

    if not os.getenv("PGPASSWORD"):
        os.environ["PGPASSWORD"] = getpass.getpass("🔑 Enter PostgreSQL password: ")

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

        if os.path.exists(backup_path):
            print(f"✅ Backup saved to: {backup_path}")
        else:
            print("⚠️ Backup command finished, but file not found.")

    except subprocess.CalledProcessError as e:
        print("❌ Backup failed (process error):", e)
    except FileNotFoundError:
        print("❌ pg_dump not found. Please install PostgreSQL or add it to PATH.")

def run():
    perform_backup()

if __name__ == "__main__":
    run_tool_template(run, "PostgreSQL Backup Tool")
