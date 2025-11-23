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

# MODULE 2: Book Inventory Management
# Handles viewing and modifying the primary book list.

def view_available_books(books):
    """Displays the list of all books in the inventory."""
    print("\nAvailable Books:")
    if len(books) > 0:
        for book in books:
            print(books)
            break
    else:
        print("No books available.")

def add_book(books):
    """Adds a new book or updates the stock of an existing one."""
    while True:
              bookID=int(input("Enter bookID : "))
              new_book=input("Enter the name of the book to add: ")
              author=input("Enter author name : ")
              stock=int(input("Enter no.of copies : "))
              d={"bookID":bookID,"new_book":new_book,"author":author,"stock":stock}
              books[bookID]=d
              ch=input("continue? (no/yes) : ")
              if ch=="no":
                 break
    print("book has been added ---> ",d)


# MODULE 3: Transaction Management
# Handles borrowing and returning books and updates transaction records.


def borrow_book(books, borrowed_books):
    """Handles the borrowing process, reducing stock."""
    while True:
             borrow_bookID = int(input("Enter the ID of the book to borrow: "))
             if borrow_bookID in books:
                x=books[borrow_bookID]
                borrowed_books[borrow_bookID]=x
                ch=input("continue? : ")
                if ch=="no":
                   print("You have borrowed",borrowed_books)
                   break
             else:
                print("bookID",borrow_bookID,"is not available in the library.")


def return_book(books, borrowed_books, returned_books):
    """Handles the return process, increasing stock."""
    return_bookID =int(input("Enter the ID of the book to return: "))
    if return_bookID in borrowed_books:
       y=borrowed_books[return_bookID]
       returned_books[return_bookID]=y
       print(returned_books,"has been returned to the library.")
    else:
       print(return_bookID,"was not borrowed.")

if __name__ == "__main__":
    while True:
        choice = main_menu()
        
        if choice == "1":
            view_available_books(books)
        
        elif choice == "2":
            add_book(books)
        
        elif choice == "3":
            borrow_book(books, borrowed_books)
        
        elif choice == "4":
            return_book(books, borrowed_books, returned_books)
        
        elif choice == "5":
            print("Exiting the Library Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
