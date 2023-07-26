# Define the database model for the 'books' table
from services.db_service import db

class Book(db.Model):
    BookID = db.Column(db.Integer, primary_key=True)
    ISBN = db.Column(db.String(13), unique=True, nullable=False)
    Name = db.Column(db.String(255), nullable=False)
    Description = db.Column(db.Text)
    Price = db.Column(db.Float)
    AuthorID = db.Column(db.Integer, db.ForeignKey('author.AuthorID'))
    Genre = db.Column(db.String(255))
    Publisher = db.Column(db.String(255))
    YearPublished = db.Column(db.Integer)
    CopiesSold = db.Column(db.Integer)

# Define the database model for the 'authors' table
class Author(db.Model):
    AuthorID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(255), nullable=False)
    LastName = db.Column(db.String(255), nullable=False)
    Biography = db.Column(db.Text)
    Publisher = db.Column(db.String(255))