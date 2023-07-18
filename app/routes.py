from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from services.db_service import db
from models.models import Book
from . import create_app

app = create_app()

db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return jsonify(message="Hello, World!")

@app.route('/books/<genre>', methods=['GET'])
def get_books_by_genre(genre):
    books = Book.query.filter_by(genre=genre).all()
    book_list = []
    for book in books:
        book_data = {
            'id': book.id,
            'title': book.title,
            'genre': book.genre
        }
        book_list.append(book_data)
    return jsonify({'books': book_list})

@app.route('/books/most_sold', methods=['GET'])
def get_most_sold_books():
    most_sold_books = Book.query.order_by(Book.sales.desc()).limit(10).all()
    book_list = []
    for book in most_sold_books:
        book_data = {
            'id': book.id,
            'title': book.title,
            'sales': book.sales
        }
        book_list.append(book_data)
    return jsonify({'most_sold_books': book_list})

@app.route('/books/higher_rating/<float:threshold>', methods=['GET'])
def get_books_with_higher_rating(threshold):
    books = Book.query.filter(Book.rating > threshold).all()
    book_list = []
    for book in books:
        book_data = {
            'id': book.id,
            'title': book.title,
            'rating': book.rating
        }
        book_list.append(book_data)
    return jsonify({'books_with_higher_rating': book_list})

@app.route('/books/discount_publisher/<publisher>/<float:discount>', methods=['PUT'])
def discount_books_by_publisher(publisher, discount):
    books = Book.query.filter_by(publisher=publisher).all()
    for book in books:
        book.price -= (book.price * discount)
        db.session.add(book)
    db.session.commit()
    return jsonify({'message': 'Discount applied to books by publisher.'})



@app.route('/cart/subtotal', methods=['GET'])
def get_subtotal():
    try:
        user_id = int(request.args.get('userId'))
        cart_items = ShoppingCart.query.filter_by(user_id=user_id).all()
        total_price = sum(item.price for item in cart_items)
        return jsonify({'subtotal': total_price})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    try:
        data = request.get_json()
        user_id = int(data['userId'])
        book_id = int(data['bookId'])
        book = ShoppingCart.query.filter_by(book_id=book_id).first()
        if book:
            return jsonify({'error': 'Book already in cart'})
        new_cart_item = ShoppingCart(user_id=user_id, book_id=book_id, price=0.0)
        db.session.add(new_cart_item)
        db.session.commit()
        return jsonify({'message': 'Book added to cart successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/cart/books', methods=['GET'])
def get_cart_books():
    try:
        user_id = int(request.args.get('userId'))
        books = ShoppingCart.query.filter_by(user_id=user_id).all()
        book_list = [{'id': book.book_id, 'title': book.title, 'price': book.price} for book in books]
        return jsonify({'books': book_list})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/cart/delete', methods=['DELETE'])
def delete_from_cart():
    try:
        user_id = int(request.args.get('userId'))
        book_id = int(request.args.get('bookId'))
        cart_item = ShoppingCart.query.filter_by(user_id=user_id, book_id=book_id).first()
        if not cart_item:
            return jsonify({'error': 'Book not found in cart'})
        db.session.delete(cart_item)
        db.session.commit()
        return jsonify({'message': 'Book deleted from cart successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})
