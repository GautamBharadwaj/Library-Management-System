from datetime import datetime
import pandas as pd
from storage import database_manager
import logging

class checkin_checkout_manager:
    def __init__(self):
        self.database = database_manager()
        self.reload_dataframes()
    
    def reload_dataframes(self):
        self.books_df = self.database.book_db()
        self.users_df = self.database.user_db()
        self.checkouts_df = self.database.checkin_checkout_db()
    
    def checkin_book(self, isbn):
        checkout_entry = self.checkouts_df[self.checkouts_df['ISBN'] == str(isbn)]
        if checkout_entry.empty:
            logging.info("\nBook not checked out.")
            return False
        checkout_entry_index = self.checkouts_df[self.checkouts_df['CheckinTime'].isnull()].index
        self.checkouts_df.at[checkout_entry_index, 'CheckinTime'] = datetime.now()
        self.database.save_to_sql(self.checkouts_df,'checkouts')
        logging.info("\nBook checked in successfully.")
        return True
    
    def checkout_book(self, user_id, isbn):
        self.reload_dataframes()
        if str(user_id) not in self.users_df['UserID'].values:
            logging.info("\nUser does not exist.")
            return False
        if str(isbn) not in self.books_df['ISBN'].values:
            logging.info("\nBook does not exist.")
            return False
        # Check if the book is already checked out
        checkout_entry = self.checkouts_df[(self.checkouts_df['ISBN'] == str(isbn)) & (self.checkouts_df['CheckinTime'].isnull())]
        if not checkout_entry.empty:
            logging.info("\nBook is already checked out.")
            return False
        # If the book is available, add a new checkout entry
        current_time = str(datetime.now())
        new_checkout = {'UserID': user_id, 'ISBN': str(isbn), 'CheckoutTime': current_time}
        self.checkouts_df = self.checkouts_df.append(new_checkout, ignore_index=True)
        self.database.save_to_sql(self.checkouts_df, 'checkouts')
        logging.info("\nBook is checked out.")
        return True
    
    def is_book_available(self, isbn):
        self.reload_dataframes()
        checkout_entry = self.checkouts_df[(self.checkouts_df['ISBN'] == str(isbn)) & (self.checkouts_df['CheckinTime'].isnull())]
        if checkout_entry.empty:
            logging.info("\nBook is available for checkout.")
            return True
        else:
            logging.info("\nBook is checked out.")
            return False
    
    def list_all_checkout_books(self):
        self.reload_dataframes()
        return logging.info(self.checkouts_df)
    


    