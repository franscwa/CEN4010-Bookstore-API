# You'll define your SQLAlchemy models in such files
from ..services.db_service import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(200), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    publisher = db.Column(db.String(200), nullable=False)
    genre = db.Column(db.String(200), nullable=False)
    sold = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Title: %r>' % self.title
    