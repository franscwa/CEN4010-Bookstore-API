from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DBService:
    def init_app(self, app):
        db.init_app(app)
        with app.app_context():
            db.create_all()
