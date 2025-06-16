# 🧰 PostgreSQL Study Project

![License: MIT](https://img.shields.io/badge/license-MIT-green)
![DB Test](https://github.com/TamerOnLine/postgres_study_project/actions/workflows/test-db.yml/badge.svg)
<p>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" alt="PostgreSQL" width="40" title="PostgreSQL">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" alt="MySQL" width="40" title="MySQL">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" alt="SQLite" width="40" title="SQLite">
  <img src="https://img.shields.io/badge/GitHub_Actions-CI-blue?logo=github-actions&logoColor=white" alt="GitHub Actions CI" height="30">
</p>


A hands-on educational toolkit for managing PostgreSQL databases using **Python**, **SQLAlchemy**, and **psycopg2** – fully terminal-based and modular.

> Learn and manage PostgreSQL like a pro – from creating databases to restoring backups, all via CLI.

---

## 📥 Clone the Repository

To get started, clone this repository to your local machine using Git:

```bash
git clone https://github.com/TamerOnLine/postgres_study_project.git
cd postgres_study_project
```

- Make sure you have Git installed: [https://git-scm.com](https://git-scm.com)

---

## 📦 Features

- 🧠 Modular CLI tools for PostgreSQL admin tasks
- 🧱 SQLAlchemy models for clean DB interaction
- 🔄 Create, drop, and manage databases or tables interactively
- 💾 Backup and restore using `pg_dump` / `psql`
- 🧩 Environment configuration with `.env` and `python-dotenv`
- 🧪 Multi-database support: SQLite, PostgreSQL, and MySQL

---

## 🗂️ Project Structure

```
tameronline-postgres_study_project/
├── main.py                     # CLI launcher for all tools
├── config/                     # Environment and session handlers
├── models/                     # SQLAlchemy models
├── tools/                      # All database tools (PostgreSQL, tester, etc.)
└── requirements.txt 
```

---

## ⚙️ Environment Setup

Create a `.env` file in the root folder with content like:

```env
POSTGRES_DB_USER=postgres
POSTGRES_DB_PASSWORD=yourpassword
POSTGRES_DB_HOST=localhost
POSTGRES_DB_PORT=5432
POSTGRES_DB_NAME=my_database
```

You can also configure:
```env
MYSQL_DB_USER=...
SQLITE_DB_NAME=default.db
```

---

## 🚀 Quick Start

### 1. Create a virtual environment

```bash
# Windows
py -3.12 -m venv venv
.\env\Scripts\Activate
```

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Launch the main CLI

```bash
python main.py
```

You'll see a menu to select the tool you want to run interactively.

---

## 🛠️ PostgreSQL Tools

Each tool is located in `tools/db/postgres/` and can be run directly:

| Task                    | Command                                        |
|-------------------------|------------------------------------------------|
| 🏗️ Create database        | `python tools/db/postgres/create.py`          |
| ❌ Drop database          | `python tools/db/postgres/drop.py`            |
| 🧹 Drop tables            | `python tools/db/postgres/drop_table.py`      |
| 🧩 Manage schema          | `python tools/db/postgres/manage_tables.py`   |
| 💾 Backup database        | `python tools/db/postgres/backup.py`          |
| ♻️ Restore from backup    | `python tools/db/postgres/restore.py`         |
| 🔍 View table contents    | `python tools/db/postgres/view.py`            |

---

## 🔍 Test All Connections

Test PostgreSQL, MySQL, and SQLite connectivity with:

```bash
python tools/db/connection_tester/main.py
```

---

## 🧪 Development Mode

By default, the project uses `.env` to decide the environment.  
To enable protection from dangerous actions in production mode, set:

```env
FLASK_ENV=production
```

This will block destructive actions like dropping all tables.

---

## 🧩 Models Overview

Models are defined in `models/`:

```python
# Example: Product model
class Product(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Float)
```

You can customize and extend these models freely.

---

## 📂 Backup Directory

Backups are automatically saved under:

```
backups/YYYY/MM/your_backup_file.sql
```

You can choose a custom name or use the auto-generated timestamp.

---

## 🧠 Learning Purpose

This project was built for:
- Understanding PostgreSQL database operations
- Practicing CLI tools and modular code design
- Building toward future full-stack admin tools

---

## 📄 License

Licensed under the MIT License.  
See the [LICENSE](./LICENSE) file for details.

---

## 👨‍💻 Author

**Tamer Hamad Faour**  
GitHub: [@TamerOnLine](https://github.com/TamerOnLine)