import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/wishlist_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Wishlist(db.Model):
    __tablename__ = 'wishlist'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    name = db.Column(db.String(255))


class WishlistItem(db.Model):
    __tablename__ = 'wishlist_item'
    id = db.Column(db.Integer, primary_key=True)
    wishlist_id = db.Column(db.Integer, db.ForeignKey('wishlist.id'))
    book_id = db.Column(db.Integer)


class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.query(WishlistItem).delete()
            db.session.query(Wishlist).delete()
            db.session.commit()

            db.session.remove()
            db.drop_all()

    def test_something(self):
        with app.app_context():
            wishlist = Wishlist(name="My Wishlist")
            db.session.add(wishlist)
            db.session.commit()

            found_wishlist = db.session.query(Wishlist).filter_by(name="My Wishlist").first()
            self.assertEqual(found_wishlist.name, "My Wishlist")


if __name__ == '__main__':
    unittest.main()
