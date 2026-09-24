# WIP1.py - Work in progress for the DLL Developer Hub Prototype
# Early stub of the home menu and finance API catalog (Version 1, CLI).

api_catalog = [
    {"id": "quote", "name": "Quote API", "goal": "Create a finance quote"},
    {"id": "finance-app", "name": "Finance Application API", "goal": "Submit a finance application"},
    {"id": "contract", "name": "Contract API", "goal": "View contract information"},
]


def show_home_menu():
    print("=== DLL Developer Hub ===")
    print("1) API Catalog")
    print("2) Request Credentials")


def show_catalog():
    print("\nAvailable finance APIs:")
    for product in api_catalog:
        print(f"- {product['name']}: {product['goal']}")


if __name__ == "__main__":
    show_home_menu()
    show_catalog()