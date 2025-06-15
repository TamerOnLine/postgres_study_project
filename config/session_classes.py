# config/session_classes.py

from config.postgres_session import PostgresSession
from config.mysql_config import MySQLSession
from config.sqlite_config import SQLiteSession

SESSIONS = {
    "postgres": PostgresSession,
    "mysql": MySQLSession,
    "sqlite": SQLiteSession
}
