import sqlite3

connection = sqlite3.connect('MarketExchange.db')

cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR NOT NULL UNIQUE,
    balance DOUBLE,
    datecreated DATETIME NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    orders_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR,
    stock_name VARCHAR NOT NULL,
    price DOUBLE NOT NULL,
    quantity NOT NULL,
    order_type BOOLEAN NOT NULL, 
    FOREIGN KEY (user_name) REFERENCES users (user_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS trades (
    stock_id INTEGER AUTO_INCREMANT PRIMARY KEY,
    user_name
    stock_name VARCHAR NOT NULL, 
    stock_price DOUBLE NOT NULL,
    stock_quantity INT,
    datecreated DATE TIME
)
""")

connection.commit()