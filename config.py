import os
from flask import Flask, request, jsonify

app = Flask(__name__)

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://root:@localhost/wishlist_database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

