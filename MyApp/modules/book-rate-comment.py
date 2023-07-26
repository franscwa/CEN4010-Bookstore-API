#gabriel
from flask import Blueprint, jsonify, request
import mysql.connector

bp = Blueprint('book-rate-comment', __name__, url_prefix='/book-rate-comment')

@bp.route('/ratings', methods=['POST'])
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

    return jsonify({'message': 'You have left a rating'}), 200


@bp.route('/comments', methods=['POST'])
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

    return jsonify({'message': 'You have left a comment'}), 200


@bp.route('/comments/<book_id>', methods=['GET'])
def get_comments(book_id):
    # Retrieve comments for the given book ID from the 'comments' table
    query = "SELECT comment FROM comments WHERE book_id = %s"
    values = (book_id,)
    cursor.execute(query, values)
    comments = [row[0] for row in cursor.fetchall()]

    return jsonify(comments), 200

# Pulls the ratings for a given book id
@bp.route('/ratings/<book_id>', methods=['GET'])
def get_average_rating(book_id):

    query = "SELECT rating FROM ratings WHERE book_id = %s"
    values = (book_id,)
    cursor.execute(query, values)
    ratings = [row[0] for row in cursor.fetchall()]

    average_rating = find_average_rating(ratings)

    return jsonify({'average_rating': average_rating}), 200


# Calculate the average rating
def find_average_rating(ratings):
    if not ratings:
        return 0.0  # Return 0 if no ratings are available
    total_rating = sum(ratings)
    average_rating = total_rating / len(ratings)
    return round(average_rating, 2)  # Round to 2 decimal places
