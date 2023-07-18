from flask import request, jsonify
from . import create_app, db_service

app = create_app()

@app.route('/')
def hello_world():
    return jsonify(message="Hello, World!")
