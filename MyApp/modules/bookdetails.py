#eebad
from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Goukou400@localhost/api'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


bp = Blueprint('book-details', __name__, url_prefix='/book-details')


# Endpoint for creating a new book
# Endpoint for creating a new book
@bp.route('/books', methods=['POST'])
def create_book():
    # Extract book data from the request
    book_data = request.get_json()

    # Insert book data into the database
    new_book = Book(
        ISBN=book_data['isbn'],
        Name=book_data['name'],
        Description=book_data['description'],
        Price=book_data['price'],
        AuthorID=book_data['author_id'],
        Genre=book_data['genre'],
        Publisher=book_data['publisher'],
        YearPublished=book_data['year_published'],
        CopiesSold=book_data['copies_sold']
    )
    db.session.add(new_book)
    db.session.commit()

    # Return a JSON response indicating successful book creation
    return jsonify({'message': 'Book created successfully'}), 201

# Endpoint for retrieving a book by ISBN
@bp.route('/books/<isbn>', methods=['GET'])
def get_book(isbn):
    # Retrieve book data from the database
    book = Book.query.filter_by(ISBN=isbn).first()

    if book is not None:
        # Create a dictionary with book data
        book_data = {
            'isbn': book.ISBN,
            'name': book.Name,
            'description': book.Description,
            'price': book.Price,
            'author_id': book.AuthorID,
            'genre': book.Genre,
            'publisher': book.Publisher,
            'year_published': book.YearPublished,
            'copies_sold': book.CopiesSold
        }
        # Return the book data as a JSON response
        return jsonify(book_data), 200
    else:
        # Return a JSON response indicating book not found
        return jsonify({'message': 'Book not found'}), 404

# Endpoint for creating an author with name and more
@bp.route('/authors', methods=['POST'])
def create_author():
    # Extract author data from the request
    author_data = request.get_json()

    # Insert author data into the database
    new_author = Author(
        FirstName=author_data['first_name'],
        LastName=author_data['last_name'],
        Biography=author_data['biography'],
        Publisher=author_data['publisher']
    )
    db.session.add(new_author)
    db.session.commit()

    # Return a JSON response indicating successful author creation
    return jsonify({'message': 'Author created successfully'}), 201

# Endpoint to retrieve list of books associated with an author
@bp.route('/authors/<int:author_id>/books', methods=['GET'])
def get_books_by_author(author_id):
    # Retrieve books data from the database for the given author
    books = Book.query.filter_by(AuthorID=author_id).all()

    if books:
        # Create a list of dictionaries with book data and return it as JSON response
        books_data = []
        for book in books:
            book_data = {
                'isbn': book.ISBN,
                'name': book.Name,
                'description': book.Description,
                'price': book.Price,
                'author_id': book.AuthorID,
                'genre': book.Genre,
                'publisher': book.Publisher,
                'year_published': book.YearPublished,
                'copies_sold': book.CopiesSold
            }
            books_data.append(book_data)
        return jsonify(books_data), 200
    else:
        # Return a JSON response indicating no books found for the given author
        return jsonify({'message': 'No books found for this author'}), 404
