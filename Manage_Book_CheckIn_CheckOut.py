from datetime import datetime
import pandas as pd
from storage import DatabaseManager
from custom_logging import setup_logging
import logging
# Configure logging
#setup_logging()

class Check_In_Check_Out:
    def __init__(self):
        self.database = DatabaseManager()
        self.books_df = self.database.BookDB()
        self.users_df = self.database.UserDB()
        self.checkouts_df = self.database.BookCheckOutCheckIn()
    
    def checkin_book(self, isbn):
        checkout_entry = self.checkouts_df[self.checkouts_df['ISBN'] == str(isbn)]
        if checkout_entry.empty:
            logging.info("\nBook not checked out.")
            return False
        checkout_entry_index = checkout_entry.index[0]
        self.checkouts_df.at[checkout_entry_index, 'CheckinTime'] = datetime.now()
        self.database.save_to_sql(self.checkouts_df,'checkouts')
        logging.info("\nBook checked in successfully.")
        return True
    
    def checkout_book(self, user_id, isbn):
        if isbn in self.checkouts_df['ISBN'].values:
            logging.info("\nBook is already checked out.")
            return False
        if user_id not in self.users_df['UserID'].values:
            logging.info("\nUser not exist.")
            return False
        if isbn not in self.books_df['ISBN'].values:
            logging.info("\nBook does not exist.")
            return False
        current_time = datetime.now()
        new_checkout = {'UserID': user_id, 'ISBN': str(isbn), 'CheckoutTime': current_time}  # Convert ISBN to string
        self.checkouts_df = self.checkouts_df.append(new_checkout, ignore_index=True)
        self.checkouts_df['UserID'] = self.checkouts_df['UserID'].astype(str)
        self.checkouts_df['ISBN'] = self.checkouts_df['ISBN'].astype(str)
        self.database.save_to_sql(self.checkouts_df,'checkouts')
        logging.info("\nBook is checked out.")
        return True
    
    def is_book_available(self, isbn):
        checkout_entry = self.checkouts_df[self.checkouts_df['ISBN'] == str(isbn)]
        if checkout_entry.empty:
            logging.info("\nBook is available for checkout.")
            return True
        else:
            logging.info("\nBook is checked out.")
            return False
    
    def list_all_checkout_books(self):
        return logging.info(self.checkouts_df)