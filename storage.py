import pandas as pd
import sqlite3

class database_manager():

    def __init__(self):    
        self.conn = sqlite3.connect("library_management_system.db")
        self.cur = self.conn.cursor()
    
    def save_to_sql(self, df, table_name):
        df.to_sql(table_name, self.conn, if_exists='replace', index=False)

    def book_db(self):    
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='books'")
        table_exists = self.cur.fetchone()
        if table_exists:
            self.books_df = pd.read_sql_query("SELECT * FROM books", self.conn)
        else:    
            self.books_df = pd.DataFrame(columns=['Title', 'Author', 'ISBN'])
            self.books_df.to_sql('books', self.conn, if_exists='replace',index=False)
        return self.books_df
        
    def user_db(self):
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        table_exists = self.cur.fetchone()
        if table_exists:
            self.users_df = pd.read_sql_query("SELECT * FROM users", self.conn)
        else:    
            self.users_df = pd.DataFrame(columns=['Name', 'UserID'])
            self.users_df.to_sql('users', self.conn, if_exists='replace',index=False)
        return self.users_df
    
    def checkin_checkout_db(self):
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='checkouts'")
        table_exists = self.cur.fetchone()
        if table_exists:
            self.checkouts_df = pd.read_sql_query("SELECT * FROM checkouts", self.conn)
        else:    
            self.checkouts_df = pd.DataFrame(columns=['UserID', 'ISBN', 'CheckoutTime', 'CheckinTime'])
            self.checkouts_df.to_sql('checkouts', self.conn, if_exists='replace',index=False)
        return self.checkouts_df