from flask import Flask
from .services.db_service import DBService

db_service = DBService()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():
        db_service.init_app(app)
        
    from . import routes
    
    return app
