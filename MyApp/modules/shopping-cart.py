from flask import Flask, request, jsonify, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from services.db_service import db
from models.Book import Book

bp = Blueprint('shopping-cart', __name__, url_prefix='/shopping-cart')

@bp.route('/')
def hello_world():
    return jsonify(message="Hello, World!")

@bp.route('/books/<genre>', methods=['GET'])
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

@bp.route('/books/most_sold', methods=['GET'])
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

@bp.route('/books/higher_rating/<float:threshold>', methods=['GET'])
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

@bp.route('/books/discount_publisher/<publisher>/<float:discount>', methods=['PUT'])
def discount_books_by_publisher(publisher, discount):
    books = Book.query.filter_by(publisher=publisher).all()
    for book in books:
        book.price -= (book.price * discount)
        db.session.add(book)
    db.session.commit()
    return jsonify({'message': 'Discount applied to books by publisher.'})
