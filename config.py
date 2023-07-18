import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Goukou400@localhost/api'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
