# MODULE 1 Initialize library data

books = {}
borrowed_books = {}
returned_books = {}

def main_menu():
    """Displays the menu and handles user choice."""
    print("=== Library Management System ===")
    print("1. View Available Books")
    print("2. Add a Book")
    print("3. Borrow a Book")
    print("4. Return a Book")
    print("5. Exit")
    return input("Enter your choice (1-5): ").strip()
