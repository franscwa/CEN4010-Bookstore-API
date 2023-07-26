from flask_mysqldb import MySQL

mysql = MySQL()

# Database configuration
def configure_database(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'wishlist_database'
    mysql.init_app(app)
