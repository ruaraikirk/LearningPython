# Library System - a small library system to describe and keep track of books using dictionaries.
# Name: Ruarai Kirk
# Student ID: D17125381
# Course: DT265A

# Below are the specific functions of the Library System:
# A Python function that prints details about all the books in the library.
def print_all(dict):
    print("There are", len(dict),"titles in stock.")
    print("The stock available is as follows:")
    for key, val in dict.items():
        print("ISBN:", key, "Title:", val[0], "Author:", val[1], "Quantity in stock:", val[2])
    return
# A Python function that adds a book to the library
def add_stock(key,details,quantity,dict):
    # The function takes the book isbn, details (as a list) and quantity purchased, as well as the library dictionary name
    if len(key) != 13: # If ISBN number is not 13 digits, send error message and exit
        print("ISBN invalid!")
        return
    else: # Otherwise, enter if-else loop
        if key in dict: # If ISBN already in the library, just update the quantity
            dict[key][2] += quantity
        else: # Else add book to the library as a new item in the dictionary
            dict[key] = details
    return
# A Python function that checks out a book for loaning
def check_out(key, dict):
    # The function takes the book isbn and the library dictionary name
    if len(key) != 13: # If ISBN number is not 13 digits, send error message and exit
        print("ISBN invalid!")
        return
    else:
        if key in dict and dict[key][2] != 0: # If ISBN valid, and there are titles in stock
            dict[key][2] -= 1 # Decrement quantity value and return message, stating success of operation and stock remaining
            print("Book checked out! There are ", dict[key][2], " copies of this title left in stock.")
        elif key not in dict: # If book ISBN not valid/does not exist, return error message
            print("Book not valid...")
        elif dict[key][2] == 0: # If book out of stock, return message
            print("This book is out of stock...")
        else:
            return
# A Python function that searches the library for a book by the book "title" and returns the book’s ISBN
def title_search(title, dict):
    for key in dict.keys():
        if dict[key][0] == title:
            print("The ISBN for book titled", title, "is", key)
            break
        #elif dict[key][0] != title:
         #   continue
        #else:
         #   return

# Library
# The library is implemented as a dictionary, with the keys being the book ISBN (13-digits) and the values being the
# details (such as title, author and quantity) implemented in a list
library = {
    "9780132805575" : ["The Practice of Computing Using Python", "William Punch", 0],
    "9780132737968" : ["Digital Fundamentals", "Thomas Floyd", 1],
    "9781118063330" : ["Operating System Concepts", "Abraham Silberschatz", 1]
           }

# User interface presented as a list of options
print("""
Library System Options:
-----------------------------
1: View details of all books in library
2: Add new stock or update quantity
3: Check out a book on loan
4: Search the library for a title and retrieve title ISBN
5: Exit Program
""")

option = int(input("Enter an option: ")) # Ask for user input

while option != 0: # While loop which process option input
    if option == 1: # Run 'view all details' function
        print_all(library)
    elif option == 2: # Run add stock (or update quantity)' function
        in1 = input("To add book, please enter the book 13-digit ISBN: ")
        in2 = str(input("Please enter book title: "))
        in3 = str(input("Please enter author: "))
        in4 = int(input("Please enter quantity purchased: "))
        details = [in2, in3, in4]
        add_stock(in1, details, in4, library)
        print_all(library)
    elif option == 3: # Run 'check out for loan' function
        in1 = input("To search for a book and borrow 1 copy, please enter the book's 13-digit ISBN: ")
        check_out(in1, library)
    elif option == 4: # Run 'search the library for a title and retrieve title ISBN' function
        in1 = input("To search for a book and retrieve it's ISBN, please enter the book's title: ")
        title_search(in1, library)
    elif option == 5: # Terminate program
        break
    elif option != 0: # If input invalid return error message and ask for input again
        print("You did not enter a valid number.")
    option = int(input("Enter an option: "))

# Notes for further improvement:
# 1. When searching for a book's isbn using the title, the title has to be inputted exactly (case sensitive etc.)
# To improve this, I would implement an all lower case value in the library, and strip the user input of case using the
# ascii 'lowercase method.

# 2. The title search function only returns a value when successful. This should be amended to return a message with a
# negative value or error message if required.

# 3. At present, the above library system only records number of books 'in stock', and not total quantity. The above
# should be amended to show this by including another value in the value list.
