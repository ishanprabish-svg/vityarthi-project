1. Problem Statement

BACKGROUND
    
Old-school library work means writing down who borrows what by hand - this takes ages, leads to mistakes, also runs slow. Tiny libraries or schools, even neighborhood spots plus personal shelves, usually don't have cheap tech tools that help them follow books properly or handle lending without hassle.

THE CHALLENGE

A basic setup should work easily for everyone - something clear, no confusion. It’s gotta be handy without being tricky to use. The goal? Keep it straightforward but still helpful. No fluff, just stuff that actually works
Maintain precise logs of book stock using varied formats now then
Keep tabs on what books are out + who’s got them
Process book returns efficiently
Show whether books are available right now
Slash the piles of paper tasks while cutting down mistakes made by people
Get into library details fast using a simple path that skips delays

Solution
The Library Management System runs on Python and works through simple commands to handle everyday tasks. Instead of costly tools or heavy setups, it uses a clear 

menu approach for tracking books. Users can check out titles or bring them back with minimal steps. This setup keeps data neat while skipping complicated designs.

2. Scope of the Project

In-Scope Features

Current Implementation (Version 1.0)

Book Inventory ManagementAdd new books with unique identifiers (Book ID)

Keep track of book info: name of the book, who wrote it, also how many copies are available

Check out all the books you can borrow at the library

Helps you manage several versions of one title

Borrowing SystemAllow users to borrow books by entering Book ID

Check if the book’s ready before you take it

Keep tabs on loaned books apart from what’s left in stock

Borrow several books at once during one visit

Return SystemProcess book returns using Book ID

Check if someone really took the book

Maintain logs of books brought back

Update transaction history

User interface with clear numbers, just pick from 1 to 5 choices

Simple directions plus quick replies

Simple move from one task to another without hassle

Graceful exit functionality

Data ManagementIn-memory storage using Python dictionaries

Keep tabs on books you own, ones lent out, also those handed back

Data sticks around while the app runs - keeps info handy till you close it

Out-of-Scope (Future Enhancements)

Not Included in Current Version:Persistent data storage (database or file system)

User verification with several people using at once

Keep track of deadlines - get alerts when they’re past due

Fine calculation for late comebacks

Smart search tools with handy filters

Book reservation system

Stock levels change by themselves after someone takes or brings back items

ISBN setup plus sorting books by type

Graphical User Interface (GUI)

Email notifications

Creating reports along with data insights

Linking up with outside library systems

Project Limitations

Data vanishes once the app stops running - storage isn't saved between uses

No support for multiple users at once

Limited error checks if users type something wrong

No ID needed from borrowers - no personal records either

Stock levels get monitored - yet they don't refresh right away when sales or transfers happen

Simple checks - no full cleanup of user data

3. Target Users

Primary Users

1. Small Library Administrators
Run book collections at schools, universities, or local hubs - while guiding access through organized setups that support learning outside classrooms
Want simple digital tools - no fancy programs
Limited tech skills yet need smooth book management
Got a new book? Add it fast. Need to know if it’s on shelf? Check right away. Handling day-to-day checkouts or returns? Get it done without hassle

2. Personal Book Collection Owners
Folks who own tons of books at home
Lend books to your pals - share them with relatives or coworkers instead
Need to know who took which item
Use Case: Maintain organized records of personal lending activities

3. Community Center Librarians
Run tiny local book spots
Manage a fair number of books coming in and out
Want cheaper ways to handle things
Run a book lending system for locals - see which titles get checked out most

4. School/College Project Students
Young people studying computers or tech who are just starting to code
Want hands-on work to get how coding really works
Looking to set up practical uses
Use Case: Learn Python programming, understand CRUD operations, practice problem-solving
Secondary Users

5. Hobby Book Club Coordinators
Keep track of books everyone shares in reading groups
Keep tabs on who’s got what book
Set up times for swapping books between folks
Use Case: Maintain club library inventory and member borrowing records

6. Small Business Owners
Cafés mixed with work spots that share books
Boutique bookshops that also rent out books
Want basic tracking but don’t want to spend much
Let people borrow books - add this option alongside what you already offer

7. Home-School Educators
Run schools' book collections
Keep tabs on who’s got which book among different kids
Want basic admin helpers
Use Case: Organize curriculum materials and track student usage
User Characteristics
Technical Proficiency: Basic to intermediate computer skills
From age 15 up - covers teens, grown-ups, older folks
Environment: Access to computer with Python installed
Time Investment: Minimal training required (5-10 minutes)
Language: English-speaking users (current version)

4. High-Level Features
Feature Category 1: Book Management

F1.1 - Add Book

Description: Put fresh books into the library stock using full info
Inputs: Book ID, Title, Author, Stock Quantity
Output: Confirmation message with book details
Business Value: Maintains up-to-date inventory of all library resources

F1.2 - View Available Books

Description: Show a full list of every book in the library
Inputs: User selects menu option
Shows a sorted list with every book entry
Business Value: Gives a fast snapshot of the library’s books whenever needed

Feature Category 2: Transaction Processing

F2.1 - Borrow Book

Description: Handle book loan requests by checking if they’re in stock
Inputs: Book ID to borrow
Got the loan? You'll see a success note. If not, an error shows up instead
Checks whether the book’s in stock before moving forward

Speeds up checkouts while stopping people from grabbing books that aren't there

F2.2 - Return Book

Description: Handle returned books from patrons while adjusting the library’s inventory system accordingly
Inputs: Book ID being returned
Got it back fine - or error if the book was never checked out
Checks if someone really took the book out first - then allows it to be brought back
Business Value: Maintains accurate circulation records and book availability

Feature Category 3: Record Keeping

F3.1 - Borrowed Books Tracking

Maintain a distinct list for books checked out now
Keeps itself up to date whenever someone takes a book
Shows exactly which books are out right now - helping track what’s where. Keeps things open so no guessing who's got what. Makes it easier to manage without 

hassle or delays

F3.2 - Returned Books History

Store past details of every book given back
Functionality: Logs all return transactions
Business Value: Enables transaction auditing and usage pattern analysis

Feature Category 4: User Interface

F4.1 - Main Menu Navigation

Cool spot to grab every tool you need
Components: 5 numbered options with clear descriptions
User Experience: Simple, intuitive navigation requiring only number input

Business Value: Reduces learning curve and improves user adoption

F4.2 - Input Validation

Check what users type, then give clear hints if something’s wrong
Validation Types: Book ID existence, menu choice validity
Error Handling: Clear messages guiding users to correct actions

Business Value: Prevents system errors and improves user experience

F4.3 - Continuous Operation Mode

Description: Handle several tasks at once without needing to restart the app
Features a menu that runs in a cycle, stops only when you choose to quit
Business Value: Improves efficiency for batch operations

Feature Category 5: Data Management

F5.1 - In-Memory Data Storage

Description: Session-based data persistence using Python dictionaries
Store data using three distinct dicts - one for books, one for loans, another for returns
Performance: Fast read/write operations

Business Value: Lightweight solution without external dependencies

F5.2 - Data Integrity

Mix things up between every storage spot
Functionality: Coordinated updates when transactions occur
Business Value: Ensures accurate and reliable information
Success Criteria
The project counts as a win once:
All five menu choices work fine - no glitches pop up here
Books get added, then users borrow them or send them back without issues
The system keeps close tabs on which books are in stock
People might do several things at once during a visit
Fault alerts show up when actions don't work right
The setup works smoothly after just a bit of practice - no hassle at all
