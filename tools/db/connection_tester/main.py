import os
import sys

# ✅ ضبط المسار الجذر للمشروع
CURRENT = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(CURRENT, "../../../"))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# ✅ الاستيراد بعد إضافة الجذر
try:
    from config.db_config import test_all_connections
except ImportError as e:
    print(f"❌ Failed to import test_all_connections from db_config.py: {e}")
    sys.exit(1)

def main():
    print("\n🔍 Testing all database connections...\n")
    test_all_connections()
    print("\n✅ Done testing connections.\n")

def show_menu():
    main()

if __name__ == "__main__":
    show_menu()
