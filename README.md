# Ebookstore Management System
Overview
The Ebookstore Management System is a simple command-line application that allows users to manage a collection of books in an SQLite database. Users can add, update, delete, and search for books using an interactive menu.

Features
- **Create Database**: Initializes the `ebookstore.db` SQLite database and creates a `book` table if it does not exist.
- **Enter New Book**: Adds a new book to the database with details such as ID, title, author, and quantity.
- **Update Existing Book**: Allows updating a book's title, author, or quantity.
- **Delete Book**: Removes a book from the database using its ID.
- **Search Books**: Searches for books by title or author.
- **User-friendly Menu**: Provides a simple menu-driven interface to perform operations.

Installation and Usage
Prerequisites
- Python 3.x installed
- SQLite3 (bundled with Python by default)

Installation Steps
1. Clone this repository:
   ```sh
   git clone https://github.com/MendyHans/ebookstore.git
   ```
2. Navigate to the project directory:
   ```sh
   cd ebookstore
   ```
3. Run the script:
   ```sh
   python capstone_project_databases.py
   ```

Usage
Once the script is running, you will be presented with a menu:
1. **Enter Book**: Add a new book to the database.
2. **Update Book**: Modify an existing book's details.
3. **Delete Book**: Remove a book by its ID.
4. **Search Books**: Search for a book by title or author.
5. **Exit**: Close the program.

Database Structure
The `book` table is structured as follows:
| Column | Data Type | Description |
|--------|----------|-------------|
| id | INTEGER (Primary Key) | Unique identifier for the book |
| title | TEXT | Book title |
| author | TEXT | Book author |
| qty | INTEGER | Quantity available |

Example Interaction
```
Bookstore Management System
1. Enter book
2. Update book
3. Delete book
4. Search books
0. Exit
Enter your choice: 1
Enter book ID: 3007
Enter book title: The Alchemist
Enter book author: Paulo Coelho
Enter book quantity: 20
Book added successfully!
```

License
This project is licensed under the MIT License.

## Author
MendyHans


