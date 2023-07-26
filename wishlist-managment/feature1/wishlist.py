from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import models

app = Flask(__name__)

# Database configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'wishlist_database'

mysql = MySQL(app)

# initialize database if not exists
def init_db():
    cur = mysql.connection.cursor()
    cur.execute('''  
        CREATE TABLE IF NOT EXISTS wishlist (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            name VARCHAR(255) NOT NULL
        ) 
        ''')
    cur.execute(''' 
        CREATE TABLE IF NOT EXISTS wishlist_item (
            id INT AUTO_INCREMENT PRIMARY KEY,
            wishlist_id INT NOT NULL,
            book_id INT NOT NULL,
            FOREIGN KEY (wishlist_id) REFERENCES wishlist(id)
        ) 
        ''')
    cur.execute(''' 
        CREATE TABLE IF NOT EXISTS book (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL
        ) 
        ''')
    mysql.connection.commit()

# Creates tables if not exist
with app.app_context():
    init_db()

@app.route('/wishlist', methods=['POST'])
def create_wishlist():
    cur = mysql.connection.cursor()
    user_id = request.json['user_id']
    name = request.json['name']
    cur.execute("INSERT INTO wishlist(user_id, name) VALUES(%s, %s)", (user_id, name))
    mysql.connection.commit()

    wishlist_id = cur.lastrowid

    cur.close()

    response_data = {
        'message': 'Wishlist created successfully!',
        'wishlist_id': wishlist_id
    }
    return jsonify(response_data), 201


@app.route('/wishlist/<int:wishlist_id>/book/<int:book_id>', methods=['POST'])
def add_book_to_wishlist(wishlist_id, book_id):
    try:
        cur = mysql.connection.cursor()

        # Checks if the wishlist exists before inserting the book
        cur.execute("SELECT id FROM wishlist WHERE id = %s", (wishlist_id,))
        result = cur.fetchone()

        if result:
            # Inserts the book into the wishlist_item table
            cur.execute("INSERT INTO wishlist_item (wishlist_id, book_id) VALUES (%s, %s)", (wishlist_id, book_id))
            mysql.connection.commit()
            cur.close()
            return jsonify({'message': 'Book added to wishlist successfully!'}), 201
        else:
            cur.close()
            return jsonify({'message': f'Wishlist with ID {wishlist_id} does not exist'}), 404

    except Exception as e:
        return jsonify({'message': f'Error: {e}'}), 500


@app.route('/wishlist/<int:wishlist_id>/books', methods=['GET'])
def get_books_in_wishlist(wishlist_id):
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT book.id, book.title, book.author
        FROM book
        INNER JOIN wishlist_item ON book.id = wishlist_item.book_id
        WHERE wishlist_item.wishlist_id = %s
    ''', (wishlist_id,))
    books = [dict(id=row[0], title=row[1], çauthor=row[2]) for row in cur.fetchall()]
    cur.close()

    if not books:
        return jsonify({'message': 'There are no books in existence for this wishlist'}), 404

    return jsonify(books), 200


@app.route('/wishlist/<int:wishlist_id>/book/<int:book_id>', methods=['DELETE'])
def remove_book_from_wishlist(wishlist_id, book_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM wishlist_item WHERE wishlist_id=%s AND book_id=%s", (wishlist_id, book_id))
    mysql.connection.commit()
    cur.close()
    if cur.rowcount == 0:
        return jsonify({'message': 'No such book in the wishlist'}), 404
    else:
        return jsonify({'message': 'Book removed from wishlist successfully!'}), 200


        if book_info:
            book_data = {
                'id': book_info['id'],
                'title': book_info['title'],
                'author': book_info['author'],
            }
            book_list.append(book_data)

    return jsonify(book_list), 200



if __name__ == "__main__":
    app.run(debug=True)
