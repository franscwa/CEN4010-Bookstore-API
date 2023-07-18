from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    home_address = db.Column(db.String(100))

    def __init__(self, username, password, name=None, email=None, home_address=None):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.home_address = home_address

class CreditCard(db.Model):
    __tablename__ = 'credit_cards'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), db.ForeignKey('users.username'), nullable=False)
    card_number = db.Column(db.String(16), nullable=False)
    expiry_date = db.Column(db.String(5), nullable=False)
    cvv = db.Column(db.String(4), nullable=False)

    def __init__(self, username, card_number, expiry_date, cvv):
        self.username = username
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv
