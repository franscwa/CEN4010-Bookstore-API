import os
from flask import Flask, request, jsonify

app = Flask(__name__)

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Goukou400@localhost/api'

=======
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://root:@localhost/wishlist_database'
>>>>>>> 6c3f04012a03db754fb33c6ac35054fa1bac08d8
    SQLALCHEMY_TRACK_MODIFICATIONS = False

