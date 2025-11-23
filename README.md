1. Project Title

Library Management System - A Python Command-Line Application

2. Overview of the Project

The Library Management System works through the command line using Python, acting like a mini digital library setup. It lets staff or visitors handle book lists, check who’s borrowed what, also see when items get returned. Users can keep tabs on every action happening in the library, sort of like a logbook for daily tasks. Built around core coding ideas - like organizing info with dictionaries, guiding steps via conditions, reusing code blocks as functions, while responding to typed commands - it keeps things running smoothly.
The setup keeps book records split into three parts - added titles, checked-out copies, or ones brought back - so handling everything from getting new books to tracking who’s using them works smoothly.

3. Features

Core Functionality

Check out the books we’ve got → see every title along with info like author or genre. Each entry shows what’s on hand so you know exactly what’s available

Put in books: toss a fresh book into the mix using its ID, name, writer, along with how many copies are ready

Borrow Books: Let people take books from the library stock now or later - using a quick scan or online sign-in, maybe even through an app that tracks due dates automatically

↩️ Give Back Books: Handle returned books then adjust the library’s tracking info
Keep track of loans + returns using different logs

💾 In-Memory Storage: Uses Python dictionaries for efficient data management

Keeps going: lets you run several tasks one after another without stopping

✅ Input Validation: Verifies book availability before borrowing

A clear menu with numbers - so you can move around without hassle

4. Tools Used

Programming Language
Python 3.x - Core programming language
Development Tools
Python Standard Library - Built-in functions and data structures
Text Editor/IDE - Any Python-compatible editor (VS Code, PyCharm, IDLE, etc.)
Command Line/Terminal - For running the application
Data Structures
Dictionaries – To keep track of books, also what’s been checked out, or brought back
Words – Handling what users type plus sorting text stuff
Integers - For book IDs and stock quantities

5. Steps to Run the Project
Prerequisites
Make sure Python 3.x is on your computer. Try checking it like this:


bash
or


bash
Installation and Execution
Clone or Download the Repository


bash
Navigate to Project Directory


bash
Run the Application


bash
or


bash
Go through the display guide. You’ll see a list - pick from choices numbered one to five
Enter your choice and press Enter
Stick to the hints given for every task

6. Instructions for Testing

Test Case 1: Adding Books
Run the program
Select option 2 (Add a Book)
Enter test data:
Book ID: 101
Book Name: Python Programming
Author: John Smith
Stock: 5
Type no if you're prompted to go on
Book gets added - confirmation shows up right after

Test Case 2: Viewing Books
After adding books (Test Case 1)
Select option 1 (View Available Books)
Should show the books list - includes every book put in

Test Case 3: Borrowing a Book
First add a book (follow Test Case 1)
Select option 3 (Borrow a Book)
Enter the book ID: 101
Type no if you don't want to go on
Expected Result: Should display borrowed books with confirmation message

Test Case 4: Borrowing Non-Existent Book
Select option 3 (Borrow a Book)
Put in a book number that isn’t real - like 997
Expected Result: Should display error message "bookID 999 is not available in the library."

Test Case 5: Returning a Borrowed Book
First borrow a book (follow Test Case 3)
Select option 4 (Return a Book)
Enter the borrowed book ID: 101
Should show a message saying the book was handed back

Test Case 6: Returning Non-Borrowed Book
Select option 4 (Return a Book)
Put in a book number that hasn't been taken out: 888
Expected Result: Should display message "888 was not borrowed."

Test Case 7: Complete Workflow
Add several books - ID numbers 101, 102, 103 - using batch entry
View all books
Borrow book ID 101 - also grab 102 if you need it
Give back a single book (ID: 101)
View available books
All tasks must finish without issues, showing clear feedback
Test Case 8: Exit Program
Pick number 5 - or just leave
Expected Result: Program should display goodbye message and terminate
Testing Tips
Try different kinds of data to check if input handling works right
Give wrong menu picks now and then - see how errors get managed
Try weird situations - say, no items in stock
Run several steps one after another to check if data stays safe while the system runs
Known Issues to Test
The view_available_books() function could use tweaks so books show up right
Book stock numbers don’t change right now while someone borrows or gives back a book
Several people can't check out one copy at once right now

# OUTPUT 1
<img width="933" height="544" alt="image" src="https://github.com/user-attachments/assets/f84be44a-cb5e-4088-8472-54ccd626b087" />

# OUTPUT 2
<img width="932" height="547" alt="image" src="https://github.com/user-attachments/assets/d640e5bf-fecb-42e3-b2f5-90f01edf1907" />

# OUTPUT 3
<img width="929" height="548" alt="image" src="https://github.com/user-attachments/assets/f5ee9ccd-f40c-4fa6-bfc4-3839132805b0" />
