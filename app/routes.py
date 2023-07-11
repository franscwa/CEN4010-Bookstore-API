from flask import request, jsonify
from . import create_app, db_service

app = create_app()

@app.route('/')
def hello_world():
    return jsonify(message="Hello, World!")

@app.route('/byGenre')
def booksByGenre():
    return "", 204

@app.route('/byTopSellers')
def booksByTopSellers():
    return "", 204

@app.route('/byRating')
def booksByRating():
    return "", 204

@app.route('/byPublisher', methods=['PUT'])
def booksByPublisher():
    return "", 204