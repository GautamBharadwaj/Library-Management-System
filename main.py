import pandas as pd
from book import book_manager
from user import user_manager
from checkin_checkout import checkin_checkout_manager
from logger import setup_logging
import logging
# Configure logging
setup_logging()

def show_choices():
    df = pd.DataFrame([['1', 'Add Book'],
                       ['2', 'Update Book'],
                       ['3', 'Delete Book'],
                       ['4', 'List Book'],
                       ['5', 'Search Book'],
                       ['6', 'Add User'],
                       ['7', 'Update User'],
                       ['8', 'Delete User'],
                       ['9', 'List User'],
                       ['10', 'Search User'],
                       ['11', 'Checkout Book'],
                       ['12', 'CheckIn Book'],
                       ['13', 'Track Book Availability'],
                       ['14', 'List CheckOut Books']],
                      columns=['choices', 'Description'])
    logging.info(df)

def main():
    book_mgr = book_manager()
    user_mgr = user_manager()
    checkout_mgr = checkin_checkout_manager()
    while True:
        show_choices()
        choice = input("Enter choice: ")
        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")  
            if validate_isbn(isbn):    
                book_mgr.add_book(title, author, isbn)
        elif choice == "2":
            isbn = input("ISBN: ")
            title = input("New Title (press Enter to skip): ")
            author = input("New Author (press Enter to skip): ")
            if validate_isbn(isbn):    
                book_mgr.update_book(isbn, title, author)
        elif choice == "3":
            isbn = input("ISBN: ")
            if validate_isbn(isbn):    
                book_mgr.delete_book(isbn)
        elif choice == "4":
            book_mgr.list_books()
        elif choice == "5":
            word = input("Word: ")
            book_mgr.search_books(word)
        elif choice == "6":
            name = input("Name: ")
            user_id = input("UserID: ")
            if validate_user_id(user_id):    
                user_mgr.add_user(name, user_id)
        elif choice == "7":
            user_id = input("UserID: ")
            name = input("New Name (press Enter to skip): ")
            if validate_user_id(user_id):    
                user_mgr.update_user(name, user_id)
        elif choice == "8":
            user_id = input("UserID: ")
            if validate_user_id(user_id):    
                user_mgr.delete_user(user_id)
        elif choice == "9":
            user_mgr.list_users()
        elif choice == '10': # Checkout Book
            name = input("Name: ")
            user_mgr.search_users(name)
        elif choice == '11': # Checkout Book
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN: ")
            if validate_isbn(isbn) and validate_user_id(user_id):    
                checkout_mgr.checkout_book(user_id, isbn)
        elif choice == "12":
            isbn = input("Enter ISBN: ")
            if validate_isbn(isbn):    
                checkout_mgr.checkin_book(isbn)    
        elif choice=="13":
            isbn = input("Enter ISBN: ")
            if validate_isbn(isbn):    
                checkout_mgr.is_book_available(isbn)
        elif choice=="14":
            checkout_mgr.list_all_checkout_books()
        else:
            logging.info("Invalid choice. Please try again.")



def validate_user_id(user_id):
    if user_id.isdigit():  # Check if user_id is composed only of digits
        return True
    else:
        logging.info("Invalid UserID. UserID must be a number.")
        return False
    
def validate_isbn(isbn):
    if isbn.isdigit():
        return True
    else:
        logging.info("Invalid ISBN format. Please enter a Number.")
        return False

if __name__ == "__main__":
    main()



