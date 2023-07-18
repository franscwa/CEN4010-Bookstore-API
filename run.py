from flask import Flask, request, jsonify
import pymysql

# Create a Flask application
app = Flask(__name__)

# Connect to the MySQL database
db_connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Goukou400',
    database='api'
)

# Define table names in the database
books_table = 'books'
authors_table = 'authors'

# Create tables if they don't exist
create_books_table_query = f"""
CREATE TABLE IF NOT EXISTS {books_table} (
    BookID INT PRIMARY KEY AUTO_INCREMENT,
    ISBN VARCHAR(13) UNIQUE NOT NULL,
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2),
    AuthorID INT,
    Genre VARCHAR(255),
    Publisher VARCHAR(255),
    YearPublished YEAR,
    CopiesSold INT,
    FOREIGN KEY (AuthorID) REFERENCES {authors_table}(AuthorID)
)
"""

create_authors_table_query = f"""
CREATE TABLE IF NOT EXISTS {authors_table} (
    AuthorID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Biography TEXT,
    Publisher VARCHAR(255)
)
"""

# Execute table creation queries
with db_connection.cursor() as db_cursor:
    db_cursor.execute(create_books_table_query)
    db_cursor.execute(create_authors_table_query)

# Close the database connection
db_connection.close()

# Endpoint for creating a new book
@app.route('/books', methods=['POST'])
def create_book():
    # Extract book data from the request
    book_data = request.get_json()

    # Connect to the database
    with pymysql.connect(
        host='localhost',
        user='root',
        password='Goukou400',
        database='api'
    ) as db_connection:
        # Insert book data into the database
        insert_book_query = f"""
        INSERT INTO {books_table} (ISBN, Name, Description, Price, AuthorID, Genre, Publisher, YearPublished, CopiesSold)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        with db_connection.cursor() as db_cursor:
            db_cursor.execute(insert_book_query, (
                book_data['isbn'], book_data['name'], book_data['description'], book_data['price'],
                book_data['author_id'], book_data['genre'], book_data['publisher'], book_data['year_published'],
                book_data['copies_sold']
            ))
            db_connection.commit()

    # Return a JSON response indicating successful book creation
    return jsonify({'message': 'Book created successfully'}), 201

# Endpoint for retrieving a book by ISBN
@app.route('/books/<isbn>', methods=['GET'])
def get_book(isbn):
    # Connect to the database
    with pymysql.connect(
        host='localhost',
        user='root',
        password='Goukou400',
        database='api'
    ) as db_connection:
        # Retrieve book data from the database
        select_book_query = f"""
        SELECT * FROM {books_table} WHERE ISBN = %s
        """
        with db_connection.cursor() as db_cursor:
            db_cursor.execute(select_book_query, (isbn,))
            book = db_cursor.fetchone()

    if book is not None:
        # Create a dictionary with book data
        book_data = {
            'isbn': book[1],
            'name': book[2],
            'description': book[3],
            'price': book[4],
            'author_id': book[5],
            'genre': book[6],
            'publisher': book[7],
            'year_published': book[8],
            'copies_sold': book[9]
        }
        # Return the book data as a JSON response
        return jsonify(book_data), 200
    else:
        # Return a JSON response indicating book not found
        return jsonify({'message': 'Book not found'}), 404

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)