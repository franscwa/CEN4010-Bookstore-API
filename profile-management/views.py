from flask import Flask, request, jsonify
from flask_pymysql import PyMySQL

app = Flask(__name__)

mysql = PyMySQL(app)

# Endpoint to create a new user
@app.route('/user', methods=['POST'])
def create_user():
    # Extract information from the request
    user_data = request.get_json()
    username = user_data['username']
    password = user_data['password']
    # Optional fields
    name = user_data.get('name')
    email = user_data.get('email')
    home_address = user_data.get('home_address')

    # Insert the new user into the database
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (username, password, name, email, home_address) VALUES (%s, %s, %s, %s, %s)", 
                (username, password, name, email, home_address))
    mysql.connection.commit()
    cur.close()

    return '', 204

# Endpoint to get a user by username
@app.route('/user/<username>', methods=['GET'])
def get_user(username):
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM users WHERE username = %s", [username])
    if result > 0:
        user_data = cur.fetchone()
        return jsonify(user_data)
    else:
        return 'User not found', 404

# Endpoint to update a user
@app.route('/user/<username>', methods=['PUT', 'PATCH'])
def update_user(username):
    # Get the updated fields from the request
    updated_data = request.get_json()

    # Update the user in the database
    cur = mysql.connection.cursor()
    for key, value in updated_data.items():
        if key != 'email':
            cur.execute("UPDATE users SET {}=%s WHERE username=%s".format(key), (value, username))
    mysql.connection.commit()
    cur.close()

    return '', 204

# Endpoint to create a credit card for a user
@app.route('/user/<username>/credit_card', methods=['POST'])
def create_credit_card(username):
    # Extract credit card details from the request
    card_data = request.get_json()

    # Insert the new credit card into the database
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO credit_cards (username, card_number, expiry_date, cvv) VALUES (%s, %s, %s, %s)", 
                (username, card_data['card_number'], card_data['expiry_date'], card_data['cvv']))
    mysql.connection.commit()
    cur.close()

    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
