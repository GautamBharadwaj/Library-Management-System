import pandas as pd
from storage import database_manager
import logging

class book_manager:
    def __init__(self):
        self.database = database_manager()
        self.books_df = self.database.book_db()   

    def add_book(self, title, author, isbn):
        data = {"Title": title, "Author": author, "ISBN": isbn}
        self.books_df = self.books_df.append(data, ignore_index=True)
        self.database.save_to_sql(self.books_df,'books')

    def update_book(self, isbn, title=None, author=None):
        if title:
            self.books_df.loc[self.books_df['ISBN'] == isbn, 'Title'] = title
        if author:
            self.books_df.loc[self.books_df['ISBN'] == isbn, 'Author'] = author
        self.database.save_to_sql(self.books_df,'books')

    def delete_book(self, isbn):
        self.books_df = self.books_df[self.books_df['ISBN'] != isbn]
        self.database.save_to_sql(self.books_df,'books')

    def list_books(self):
        logging.info(self.books_df)
    
    def search_books(self, word):
        # Filter books_df based on whether 'Title' or 'Author' contains the search term
        search_result = self.books_df[self.books_df['Title'].str.contains(word, case=False) | 
                                    self.books_df['Author'].str.contains(word, case=False)]
        
        # Display the search result
        if not search_result.empty:
            logging.info("Search Results:")
            logging.info(search_result)
        else:
            logging.info("No matching books found.")
