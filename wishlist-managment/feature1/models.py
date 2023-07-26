# # Database Scripts
#
# #initialize database if not exists
# def init_db():
#     cur = mysql.connection.cursor()
#     cur.execute('''
#         CREATE TABLE IF NOT EXISTS wishlist (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             user_id INT NOT NULL,
#             name VARCHAR(255) NOT NULL
#         )
#         ''')
#     cur.execute('''
#         CREATE TABLE IF NOT EXISTS wishlist_item (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             wishlist_id INT NOT NULL,
#             book_id INT NOT NULL,
#             FOREIGN KEY (wishlist_id) REFERENCES wishlist(id)
#         )
#         ''')
#     cur.execute('''
#         CREATE TABLE IF NOT EXISTS book (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             title VARCHAR(255) NOT NULL,
#             author VARCHAR(255) NOT NULL
#         )
#         ''')
#