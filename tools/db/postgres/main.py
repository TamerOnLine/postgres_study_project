try:
    import setup_path  # يسمح بتشغيل الملف مباشرة
except ImportError:
    import os, sys
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)

from tools.db.postgres.menu import show_postgres_menu  # ✅ استيراد من ملف خارجي لتفادي الاستيراد الدائري

def run():
    show_postgres_menu()

if __name__ == "__main__":
    while True:
        show_postgres_menu()
