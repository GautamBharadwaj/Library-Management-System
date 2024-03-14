# Library Management System

## Introduction
This is a simple command-line based library management system implemented in Python. It allows users to perform various operations such as adding, updating, and deleting books, managing users, and checking in/checking out books.

## Python Version
This project was developed using Python 3.6.13.

## Getting Started
To use the system, follow these steps:
1. Clone the repository to your local machine:
    ```
    git clone https://github.com/your-username/library-management-system.git
    ```
2. Navigate to the directory:
    ```
    cd library-management-system
    ```
3. Run the main.py file:
    ```
    python main.py
    ```
4. Follow the prompts on the command-line interface to perform desired operations.

## Options
The following options are available in the command-line interface:
1. Add Book
2. Update Book
3. Delete Book
4. List Book
5. Search Book
6. Add User
7. Update User
8. Delete User
9. List User
10. Search User
11. Checkout Book
12. CheckIn Book
13. Track Book Availability
14. List CheckOut Books

## Code Folder Structure
The folder structure of the code is as follows:
- main.py: Main script to run the library management system.
- Manage_Book.py: Module for managing books (add, update, delete, list, search).
- Manage_User.py: Module for managing users (add, update, delete, list, search).
- Manage_Book_CheckIn_CheckOut.py: Module for book check-in and check-out operations.
- storage.py: Module for database management.
- custom_logging.py: Module for custom logging configuration.
- Library_Management_System.db: SQLite database file.
- app.log: Storing logging operations into a file