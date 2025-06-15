# tools/db/postgres/restore.py

import os
import sys

# 🧭 إعداد المسار الجذري للمشروع
CURRENT = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(CURRENT, "../../../"))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from base_tool_template import run_tool_template
from config.credentials_helper import get_credentials_from_env

import subprocess

# 🔍 مواقع psql المحتملة
PSQL_PATHS = [
    r"C:\Program Files\PostgreSQL\17\bin\psql.exe",
    r"C:\Program Files\PostgreSQL\15\bin\psql.exe",
    r"C:\Program Files\PostgreSQL\14\bin\psql.exe",
    "psql"  # fallback
]

def find_psql():
    for path in PSQL_PATHS:
        if os.path.exists(path):
            return path
    raise FileNotFoundError("❌ psql not found in known locations or PATH.")

def choose_backup_file(folder="./backups"):
    all_files = []
    for root, _, files in os.walk(folder):
        for f in files:
            if f.endswith(".sql"):
                all_files.append(os.path.join(root, f))

    if not all_files:
        raise FileNotFoundError("❌ No .sql backup files found in the 'backups' folder.")

    print("\n📂 Available backup files:")
    for idx, file in enumerate(all_files):
        print(f"{idx + 1}. {file}")

    while True:
        try:
            choice = int(input("Select file number to restore: "))
            if 1 <= choice <= len(all_files):
                return all_files[choice - 1]
            print("❌ Invalid number.")
        except ValueError:
            print("❌ Enter a valid integer.")

def perform_restore():
    creds = get_credentials_from_env("postgres")
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
    run_tool_template(perform_restore, "PostgreSQL Restore Tool")

if __name__ == "__main__":
    run()
