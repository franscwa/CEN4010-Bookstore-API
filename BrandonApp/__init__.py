from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/wishlist_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# creates a table in the database based on the classes
if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
