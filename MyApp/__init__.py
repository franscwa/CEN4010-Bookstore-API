from flask import Flask
from .services.db_service import DBService
from .database import configure_database

db_service = DBService()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    #SQLAlchemy database setup
    with app.app_context():
        db_service.init_app(app)

    #wishlist database setup
    configure_database(app)


    # Import and register blueprints for all modules
    from .modules import book-details, book-rate-comment, browsing, profile-management, wishlist
    app.register_blueprint(book-details.bp)
    app.register_blueprint(book-rate-comment.bp)
    app.register_blueprint(browsing.bp)
    app.register_blueprint(profile-management.bp)
    app.register_blueprint(wishlist.bp)

    return app
