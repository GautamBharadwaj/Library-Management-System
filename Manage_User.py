import pandas as pd
from storage import DatabaseManager
from custom_logging import setup_logging
import logging
# Configure logging
#setup_logging()

class User:
    def __init__(self):
        self.database = DatabaseManager()
        self.users_df = self.database.UserDB()

    def add_user(self, name, user_id):
        if user_id in self.users_df['UserID'].values:
            logging.info(f"User ID {user_id} already exists.")
            return
        data = {"Name": name, "UserID": user_id}
        self.users_df = self.users_df.append(data, ignore_index=True)
        self.database.save_to_sql(self.users_df,'users')

    def update_user(self, user_name, user_id):
        if user_id in self.users_df['UserID'].values:
            self.users_df.loc[self.users_df['UserID'] == user_id, 'Name'] = user_name
            self.database.save_to_sql(self.users_df,'users')
        else:
            logging.info(f"User ID {user_id} does not exists.")

    def delete_user(self, user_id):
        if user_id in self.users_df['UserID'].values:    
            self.users_df = self.users_df[self.users_df['UserID'] != user_id]
            self.database.save_to_sql(self.users_df,'users')
        else:
            logging.info("UserID not found")

    def list_user(self):
        logging.info(self.users_df)

    def search_user(self, word):
        # Filter users_df based on whether 'Name' contains the search term
        search_result = self.users_df[self.users_df['Name'].str.contains(word, case=False)]

        # Display the search result
        if not search_result.empty:
            logging.info("Search Results:")
            logging.info(search_result)
        else:
            logging.info("No matching users found.")
