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
