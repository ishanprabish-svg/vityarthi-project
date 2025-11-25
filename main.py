import mod1
import mod2

# MODULE 3: Transaction Management
# Handles borrowing and returning books and updates transaction records.
books = {}
borrowed_books = {}
returned_books = {}

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
        choice = mod1.main_menu()
        
        if choice == "1":
            mod2.view_available_books(books)
        
        elif choice == "2":
            mod2.add_book(books)
        
        elif choice == "3":
            borrow_book(books, borrowed_books)
        
        elif choice == "4":
            return_book(books, borrowed_books, returned_books)
        
        elif choice == "5":
            print("Exiting the Library Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")