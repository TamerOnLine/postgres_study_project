# main.py

try:
    import setup_path  # يضيف مجلد المشروع إلى sys.path
except ImportError:
    import os, sys
    ROOT = os.path.abspath(os.path.dirname(__file__))
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)

import os
import importlib

def show_main_menu():
    print("=== Project Tools ===")

    base_package = "tools.db"
    base_path = os.path.join(os.path.dirname(__file__), "tools", "db")

    # البحث عن مجلدات فيها main.py
    entries = [
        name for name in os.listdir(base_path)
        if os.path.isdir(os.path.join(base_path, name))
        and "main.py" in os.listdir(os.path.join(base_path, name))
    ]

    actions = {}
    print("0. Quit")
    for i, entry in enumerate(entries, start=1):
        label = entry.replace("_", " ").capitalize()
        actions[str(i)] = entry
        print(f"{i}. {label}")

    choice = input("Select: ").strip()

    if choice == "0":
        print("Goodbye!")
        return

    elif choice in actions:
        module_name = f"{base_package}.{actions[choice]}.main"
        try:
            module = importlib.import_module(module_name)
            # يبحث عن دالة تشغيل مناسبة
            for fn in ("run", "main", "start", "menu", "show_menu"):
                if hasattr(module, fn):
                    getattr(module, fn)()
                    return
            print(f"❌ Module '{module_name}' has no entry point.")
        except Exception as e:
            print(f"❌ Failed to load module '{module_name}': {e}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    show_main_menu()
