import sqlite3

#function to create database
def create_database():
    """Create and initialize the ebookstore database."""
    conn = sqlite3.connect("ebookstore.db")
    cursor = conn.cursor()

    #create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            qty INTEGER NOT NULL
        )
    """)

    # Prepopulate the table with initial data
    books = [
        (3001, "A Tale of Two Cities", "Charles Dickens", 30),
        (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
        (3003, "The Lion, the Witch and the Wardrobe", "C. S. Lewis", 25),
        (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
        (3005, "Alice in Wonderland", "Lewis Carroll", 12),
        (3006, "Atomic Habits", "James Clear", 15)
    ]

    cursor.executemany("INSERT OR IGNORE INTO book VALUES (?, ?, ?, ?)", books)
    conn.commit()
    conn.close()

#function to enter new book to database
def enter_book():
    """Add a new book to the database."""
    conn = sqlite3.connect("ebookstore.db")
    cursor = conn.cursor()

    #prompt to insert values to table
    id = int(input("Enter book ID: "))
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    qty = int(input("Enter book quantity: "))

    cursor.execute("INSERT INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)", (id, title, author, qty))
    conn.commit()
    conn.close()
    print("Book added successfully!")

#function to update existing book in database
def update_book():
    """Update an existing book's information."""
    conn = sqlite3.connect("ebookstore.db")
    cursor = conn.cursor()

    id = int(input("Enter the book ID to update: "))
    print("What would you like to update?")
    print("1. Title")
    print("2. Author")
    print("3. Quantity")
    choice = input("Enter your choice: ")

    if choice == "1":
        new_title = input("Enter the new title: ")
        cursor.execute("UPDATE book SET title = ? WHERE id = ?", (new_title, id))
    elif choice == "2":
        new_author = input("Enter the new author: ")
        cursor.execute("UPDATE book SET author = ? WHERE id = ?", (new_author, id))
    elif choice == "3":
        new_qty = int(input("Enter the new quantity: "))
        cursor.execute("UPDATE book SET qty = ? WHERE id = ?", (new_qty, id))
    else:
        print("Invalid choice.")
        conn.close()
        return

    conn.commit()
    conn.close()
    print("Book updated successfully!")

#function to update book
def delete_book():
    """Delete a book from the database."""
    conn = sqlite3.connect("ebookstore.db")
    cursor = conn.cursor()

    id = int(input("Enter the book ID to delete: "))
    cursor.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    print("Book deleted successfully!")

#function to search for book in database
def search_books():
    """Search for books in the database."""
    conn = sqlite3.connect("ebookstore.db")
    cursor = conn.cursor()

    #search for book in database using sql like statement for title/author
    search_term = input("Enter a search term (title or author): ")
    cursor.execute("SELECT * FROM book WHERE title LIKE ? OR author LIKE ?", (f"%{search_term}%", f"%{search_term}%"))

    #return results from search
    results = cursor.fetchall()
    if results:
        print("\nSearch Results:")
        for book in results:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}")
    else:
        print("No books found.")

    conn.close()

def main():
    """Main function to run the bookstore program."""
    create_database()

    while True:
        print("\nBookstore Management System")
        print("1. Enter book")
        print("2. Update book")
        print("3. Delete book")
        print("4. Search books")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            enter_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            search_books()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
