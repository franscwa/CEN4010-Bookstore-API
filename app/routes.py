from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db_config = {
    'host': '',
    'user': '',
    'password': '',
    'database': ''
}

# MySQL connector
db = mysql.connector.connect(**db_config)
cursor = db.cursor()


@app.route('/ratings', methods=['POST'])
def create_rating():
    data = request.get_json()
    rating = data['rating']
    user_id = data['user_id']
    book_id = data['book_id']

    # Insert rating into the ratings table
    query = "INSERT INTO ratings (rating, user_id, book_id) VALUES (%s, %s, %s)"
    values = (rating, user_id, book_id)
    cursor.execute(query, values)
    db.commit()

    return jsonify({'message': 'Rating created successfully'}), 200


@app.route('/comments', methods=['POST'])
def create_comment():
    data = request.get_json()
    comment = data['comment']
    user_id = data['user_id']
    book_id = data['book_id']

    # Insert comment into the comments table
    query = "INSERT INTO comments (comment, user_id, book_id) VALUES (%s, %s, %s)"
    values = (comment, user_id, book_id)
    cursor.execute(query, values)
    db.commit()

    return jsonify({'message': 'Comment created successfully'}), 200


@app.route('/comments/<book_id>', methods=['GET'])
def get_comments(book_id):
    # Retrieve comments for the given book ID from the 'comments' table
    query = "SELECT comment FROM comments WHERE book_id = %s"
    values = (book_id,)
    cursor.execute(query, values)
    comments = [row[0] for row in cursor.fetchall()]

    return jsonify(comments), 200

# Pulls the ratings for a given book id
@app.route('/ratings/<book_id>', methods=['GET'])
def get_average_rating(book_id):

    query = "SELECT rating FROM ratings WHERE book_id = %s"
    values = (book_id,)
    cursor.execute(query, values)
    ratings = [row[0] for row in cursor.fetchall()]

    average_rating = calculate_average_rating(ratings)

    return jsonify({'average_rating': average_rating}), 200


# Calculate the average rating
def calculate_average_rating(ratings):
    if not ratings:
        return 0.0  # Return 0 if no ratings are available
    total_rating = sum(ratings)
    average_rating = total_rating / len(ratings)
    return round(average_rating, 2)  # Round to 2 decimal places


if __name__ == '__main__':
    app.run(debug=True)
