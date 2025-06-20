import importlib

def show_postgres_menu():
    print("=== PostgreSQL Tools ===")
    
    # قائمة الأدوات المتوفرة
    actions = {
        "1": "tools.db.postgres.create",       
        "2": "tools.db.postgres.drop",         
        "3": "tools.db.postgres.drop_table",
        "4": "tools.db.postgres.backup",
        "5": "tools.db.postgres.restore", 
        "6": "tools.db.postgres.manage_tables", 
        "7": "tools.db.postgres.view",  
        
    }

    print("0. Back")
    for key, path in actions.items():
        name = path.split('.')[-1]
        label = name.replace("_", " ").capitalize()
        print(f"{key}. {label}")

    choice = input("Select: ").strip()

    if choice == "0":
        return

    module_path = actions.get(choice)
    if module_path:
        try:
            module = importlib.import_module(module_path)
            if hasattr(module, "run"):
                module.run()
            else:
                print(f"❌ The module '{module_path}' does not contain a 'run()' function.")
        except Exception as e:
            print(f"❌ Error loading module '{module_path}': {e}")
    else:
        print("❌ Invalid choice. Please select a valid option.")
