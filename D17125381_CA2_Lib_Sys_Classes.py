# Continuous Assessment 2 – Library system using CLASSES
# Ruarai Kirk - D17125381 - DT265A

# Notes for assessment:
# 1. Error Checking
#       There has been minimal error checking included in this program, which I realise is a major risk. Sufficient error checking would
#       involve many more lines of code. Some error checking which would need to be resolved from the outset would be:
#           a. Random ID generator - check that ID generated is not already in use
#           b. User input - for all aspects, especially in for the search, borrow/return, add/remove functions (when testing this program copy
#              and pasting of library item/member attributes, or careful case sensitive input, is required).

### Classes ###
# User class
class User:
    def __init__(self, user_id, name, address):
        self.user_id = user_id
        self.name = name
        self.address = address
        self.items = []
    def __str__(self):
        return "User ID: {}, Name: {}, Address: {}, Books on loan: {}".format(self.user_id, self.name, self.address, self.items)
    def get_name(self):
        return self.name
    def get_user_id(self):
        return self.user_id
    def add_to_item_list(self, item): # Method used in the 'Borrow Book' operation, which adds item to the user's list of items on loan
        self.items.append(item)
        return self.items
    def remove_from_item_list(self, item): # Method used in the 'Return Book' operation, which removes item to the user's list of items on loan
        self.items.remove(item)
        return self.items
# Library item Superclass
class LibraryItem:
    def __init__(self, library_id):
        self.__library_id = library_id
    def __str__(self):
        return "Library ID: {}".format(self.__library_id)
    def get_library_id(self):
        return self.__library_id
# Book Subclass
class Book(LibraryItem):
    def __init__(self, library_id, isbn, title, author, year):
        LibraryItem.__init__(self, library_id)
        self.__isbn = isbn
        self.__title = title
        self.author = author
        self.year = year
        self.status = "Available"
        self.borrower = []
    def __str__(self):
        return "ISBN: {}, Title: {}, Author: {}, Year: {}, Status: {}, Borrower: {}".format(self.__isbn, self.__title, self.author, self.year, self.status, self.borrower)
    def get_title(self):
        return self.__title
    def get_year(self):
        return self.year
    def get_status(self):
        return self.status
    def get_borrower(self):
        return self.borrower
    def book_out(self, rec): # Method used in the 'Borrow Book' operation, which updates the book status and adds borrower information
        self.status = "On Loan" # Update status
        self.borrower.append(rec) # Remove borrower information (in this case name)
        return self.status
    def book_in(self): # Method used in the 'Return Book' operation, which updates the book status and removes the borrower information
        self.status = "Available" # Update status
        self.borrower.clear() # Remove borrower information
# Periodical Subclass
class Periodical(LibraryItem):
    def __init__(self, library_id, title, editor, year, volume, issue):
        LibraryItem.__init__(self, library_id)
        self.__title = title
        self.editor = editor
        self.year = year
        self.volume = volume
        self.issue = issue
    def __str__(self):
        return "Title: {}, Editor: {}, Year: {}, Volume: {}, Issue: {}".format(self.__title, self.editor, self.year, self.volume, self.issue)
    def get_title(self):
        return self.__title
    def get_year(self):
        return self.year

### Functions ###
# Function that prints all library items (both books and periodicals)
def show_lib_items(library):
    print("Complete list of library items:")
    print("Books listed in library:")
    for x in library:
        if isinstance(x, Book): # If item is a book then print details
            print(x)
        else:
            continue
    print("Periodicals listed in library:")
    for x in library:
        if isinstance(x, Periodical): # After printing the books, iterate over the library items and print the periodicals
            print(x)
        else:
            continue
# Function that prints all library users
def show_lib_users(users):
    print("Library Members:")
    for x in users:
        if isinstance(x, User):
            print(x)
        else:
            continue
# Function for searching library items, by library ID
def search_lib_items_id(library, key):
    print("Search Result:")
    for x in library: # For every item in the library
        if key == x.get_library_id() and isinstance(x, Book): # If the search key (Library Item ID) equals that if the item, and it is a book, print details and break
            print("This library item is a book.")
            print(x)
            break
        elif key == x.get_library_id() and isinstance(x, Periodical): # Otherwise, if the search key (Library Item ID) equals that if the item, and it is a periodical, print details and break
            print("This library item is a periodical.")
            print(x)
            break
# Function for searching library items, by title (follows a similar approach to the above function, but with library item title as the search key)
def search_lib_items_title(library, key):
    print("Search Result:")
    for x in library:
        if key == x.get_title() and isinstance(x, Book):
            print("This library item is a book.")
            print(x)
            break
        elif key == x.get_title() and isinstance(x, Periodical):
            print("This library item is a periodical.")
            print(x)
            break
# Function for searching library items, by year of publication (follows a similar approach to the above function, but with library item publication year as the search key
def search_lib_items_year(library, key):
    print("Library items originating from the year", key)
    print("Books:")
    for x in library:
        if key == x.get_year() and isinstance(x, Book):
            print(x)
    print("Periodicals:")
    for x in library:
        if key == x.get_year() and isinstance(x, Periodical):
            print(x)
# Function for the addition of a library item, specifically a book
def add_book(library, library_id, isbn, title, author, year):
    new_book = Book(library_id, isbn, title, author, year) # From the user inputs, create new book object
    library.append(new_book) # And add the the library
    print("Book successfully added!")
# Function for the addition of a library item, specifically a periodical
def add_periodical(library, library_id, title, editor, year, volume, issue):
    new_periodical = Periodical(library_id, title, editor, year, volume, issue) # From the user inputs, create new periodical object
    library.append(new_periodical) # And add the the library
    print("Periodical successfully added!")
# Function for the addition of a library user
def add_user(users, user_id, name, address):
    new_user = User(user_id, name, address) # From the user inputs, create new user object
    users.append(new_user) # And add the the user list
    print("User successfully added!")
# Function for the removal of library items
def remove_item(library, key):
    print("Result:")
    for x in library: # for each item in the library
        if key == x.get_title(): # If search key (title) is equal to the title of the item
            print(x) # Print details and ask the user are they sure
            ans = str(input("Are you sure you want to delete this library item? (Y/N): "))
            if ans == "Y":
                library.remove(x) # If the user confirms, remove the object in the library which represents the item, otherwise return with no action
            else:
                return
# Function for the removal of library users
def remove_user(users, key):
    print("Result:")
    for x in users: # for each user in the library
        if key == x.get_name():# If search key (name) is equal to the name of the member
            print(x) # Print details and ask the user are they sure
            ans = str(input("Are you sure you want to delete this user? (Y/N): "))
            if ans == "Y":
                users.remove(x) # If the user confirms, remove the object in the library which represents the member, otherwise return with no action
            else:
                return
# Function to borrow a book
def borrow_book(library, users, title, user_id):
    for y in users: # First, get the details of the user (member) who wants to borrow a book
        if user_id == y.get_user_id(): # If the user ID number input is valid and matches a current member
            borrower = y.get_name() # Retrieve the users name, which will be used to update the book's record
            for x in library: # Now search library items for the book
                if title == x.get_title() and isinstance(x, Book) and x.get_status() == "Available": # Check that the item is in library AND that is a book AND that is it not already out on loan
                    x.book_out(borrower) # For the library item (book) object, update status to "On Load" and include borrower name (see method above)
                    y.add_to_item_list(x.get_title()) # For the library member object, update their borrowed books list
                    print("Book loaned successfully")
                elif title == x.get_title() and isinstance(x, Book) and x.get_status() == "On Loan": # But, if the book IS already out on loan
                    print("Sorry, this title is already out on loan by", x.get_borrower()) # Display notification
                else:
                    continue # If the title entered does not match the library item (book) title, continue loop
# Function to return a book
def return_book(library, users, title):
    for x in library:
        if title == x.get_title() and isinstance(x, Book) and x.get_status() == "On Loan": # Check the book details
            for y in users:
                if x.get_borrower()[0] == y.get_name(): # Retrieve the users name who borrowed the book
                    y.remove_from_item_list(title) # Remove the item (book) from their list of borrowed items (see method above)
            x.book_in() # For the library item (book) object, update status back to "Available" and remove borrower name (see method above)
            print("Book returned successfully")
        else:
            continue

### Test Data (Initial data to populate library with items and users) ###
# Test library items for library
book1 = Book("1111", "9780132805575", "The Practice of Computing Using Python", "William Punch", "2011")
book2 = Book("2222", "9780132737968", "Optimism Over Despair", "Noam Chomsky", "2017")
per3 = Periodical("3333", "Roadrunner", "Anthony Dunne", "1990", "14", "5")
# Define library item list, which stores the details of the user 'objects'
library = [book1, book2, per3]

# Test library users (aka members) for library
user1 = User("11111", "John Simpson", "16 Oak Road")
user2 = User("99999", "Sarah Jackson", "45 Cherry Lane")
# Define library user list, which stores the details of the user 'objects'
users = [user1, user2]

# Import random module for the generation of library item IDs
import random

### GUI / Menu ###
# User interface presented as a list of options
print("""
Library System Options:
-----------------------------
1: Print details of all library items
2: Print details of all library members
3: Search library items
4: Add book to library inventory
5: Add periodical to library inventory
6: Remove item from library inventory (book or periodical)
7: Add member
8: Remove member
9: Borrow book
10: Return book
11: Exit Program
""")

option = int(input("Enter an option: ")) # Ask for user input

while option != 0: # While loop which process option input
    if option == 1: # Print details of all library items
        show_lib_items(library)
    elif option == 2: # Print details of all library members(users)
        show_lib_users(users)
    elif option == 3: # Search library items will present another set of options, allowing the user to search for items via ID, title or year
        print("""
        Search library item options:
        -----------------------------
        1: Search library items by ID number
        2: Search library items by title
        3: Search library items by year
        4: Exit search
        """)
        option = int(input("Enter an option: "))  # Ask for user input
        while option != 0:  # While loop which process option input
            if option == 1:
                id_search = input("Please enter library item ID number: ")
                search_lib_items_id(library, id_search)
            elif option == 2:
                title_search = input("Please enter library item title: ")
                search_lib_items_title(library, title_search)
            elif option == 3:
                year_search = input("Please enter library item year of publication: ")
                search_lib_items_year(library, year_search)
            elif option == 4:  # Terminate search
                break
            elif option != 0:  # If input invalid return error message and ask for input again
                print("You did not enter a valid number.")
            option = int(input("Enter an option: "))
    elif option == 4: # Add book to library inventory
        in_book_id = str(random.randint(1000,9999)) # Generate 4 digit library item ID
        in_book_isbn = str(input("To add book, please enter the book 13-digit ISBN: "))
        in_book_title = str(input("Please enter book title: "))
        in_book_author = str(input("Please enter author: "))
        in_book_year = str(input("Please enter year of publication: "))
        add_book(library, in_book_id, in_book_isbn, in_book_title, in_book_author, in_book_year)
        show_lib_items(library)
    elif option == 5: # Add periodical to library inventory
        in_per_id = str(random.randint(1000,9999)) # Generate 4 digit library item ID
        in_per_title = str(input("To add periodical, please enter the periodical title: "))
        in_per_editor = str(input("Please enter periodical editor: "))
        in_per_year = str(input("Please enter year of publication: "))
        in_per_vol = str(input("Please enter volume number: "))
        in_per_issue = str(input("Please enter issue number: "))
        add_periodical(library, in_per_id, in_per_title, in_per_editor, in_per_year, in_per_vol, in_per_issue)
        show_lib_items(library)
    elif option == 6: # Remove item from library inventory (book or periodical)
        remove_item_title = str(input("To remove a library item, please enter the title: "))
        remove_item(library, remove_item_title)
        show_lib_items(library)
    elif option == 7: # Add member
        in_user_id = str(random.randint(10000, 99999)) # Generate 5 digit library user ID
        in_name = str(input("To add a new member, please enter their full name: "))
        in_address = str(input("Please enter new member address: "))
        add_user(users, in_user_id, in_name, in_address)
        show_lib_users(users)
    elif option == 8: # Remove member
        remove_name = str(input("To remove a library member, please enter their full name: "))
        remove_user(users, remove_name)
        show_lib_users(users)
    elif option == 9: # Borrow book
        borrow_book_title = input(str("Enter book title that you would like to borrow: "))
        borrow_user_id = input(str("Enter a valid User ID: "))
        borrow_book(library, users, borrow_book_title, borrow_user_id)
        show_lib_items(library)
        show_lib_users(users)
    elif option == 10: # Return book
        return_book_title = input(str("Enter book title that you would like to return: "))
        return_book(library, users, return_book_title)
        show_lib_items(library)
        show_lib_users(users)
    elif option == 11: # Terminate program
        break
    elif option != 0: # If input invalid return error message and ask for input again
        print("You did not enter a valid number.")
    option = int(input("Enter an option: "))