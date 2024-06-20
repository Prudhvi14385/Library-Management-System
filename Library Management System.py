import mysql.connector
from mysql.connector import Error

connection = None

def connect_to_database():
    global connection
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='prudhvi',
            user='root',
            password='Raj$14385'
        )
        print("Connected to the database successfully.")
    except Error as e:
        print("Error:", e)

def create_table():
    if not connection:
        connect_to_database()
    try:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                author VARCHAR(255)
            )
        ''')
        print("Table created successfully.")
    except Error as e:
        print("Error:", e)

def add_book(title, author):
    if not connection:
        connect_to_database()
    try:
        cursor = connection.cursor()
        query = "INSERT INTO books (title, author) VALUES (%s, %s)"
        data = (title, author)
        cursor.execute(query, data)
        connection.commit()
        print("Book added successfully.")
    except Error as e:
        print("Error:", e)

def view_books():
    if not connection:
        connect_to_database()
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()
        if not books:
            print("No books available.")
        else:
            print("List of books:")
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}")
    except Error as e:
        print("Error:", e)

def search_book(title):
    if not connection:
        connect_to_database()
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM books WHERE title LIKE %s"
        cursor.execute(query, ('%' + title + '%',))
        books = cursor.fetchall()
        if not books:
            print("No matching books found.")
        else:
            print("Matching books:")
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}")
    except Error as e:
        print("Error:", e)

def delete_book(book_title):
    if not connection:
        connect_to_database()
    try:
        cursor = connection.cursor()
        query = "DELETE FROM books WHERE title = %s"
        cursor.execute(query, (book_title,))
        connection.commit()
        print("Book deleted successfully.")
    except Error as e:
        print("Error:", e)

if __name__ == "__main__":
    create_table()

    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. View all books")
        print("3. Search for a book")
        print("4. Delete a book")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            add_book(title, author)

        elif choice == '2':
            view_books()

        elif choice == '3':
            search_title = input("Enter the title to search: ")
            search_book(search_title)

        elif choice == '4':
            book_id = input("Enter the title of the book to delete: ")
            delete_book(book_id)

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
