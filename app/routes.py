from flask import request, jsonify, render_template
from flask_mysqldb import MySQL
from . import create_app, db_service

app = create_app()

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'username'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'bookstore'

mysql = MySQL(app)

@app.route('/')
def hello_world():
    return jsonify(message="Hello, World!")

@app.route('/byGenre')
def booksByGenre():
    sql = mysql.connection.cursor()
    sql.execute("SELECT Name, AuthorID, Price FROM books ORDER BY Genre DESC")
    books = sql.fetchall()
    sql.close()
    return render_template('genres.html', books=books)

@app.route('/byTopSellers')
def booksByTopSellers():
    sql = mysql.connection.cursor()
    sql.execute("SELECT Name, AuthorID, Price FROM books ORDER BY CopiesSold DESC")
    books = sql.fetchall()
    sql.close()
    return render_template('genres.html', books=books)

@app.route('/byRating')
def booksByRating():
    sql = mysql.connection.cursor()
    sql.execute("SELECT Name, AuthorID, Price FROM books ORDER BY rating DESC")
    books = sql.fetchall()
    sql.close()
    return render_template('genres.html', books=books)

@app.route('/discountPublisher', methods=['POST'])
def discountPublisher():
    publisher = request.form['publisher']
    discount_percentage = request.form['new_price']

    cur = mysql.connection.cursor()
    cur.execute("UPDATE books SET price = price - (price * %s / 100) WHERE publisher = %s",
                    (discount_percentage, publisher))
    mysql.connection.commit()
    cur.close()
    return "", 204