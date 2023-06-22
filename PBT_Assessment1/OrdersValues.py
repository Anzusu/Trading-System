import sqlite3

connection = sqlite3.connect('Orders.db')

cursor = connection.cursor()

cursor.execute("INSERT or REPLACE into users (user_id, username, balance, subscription, datecreated) VALUES ('1', 'John Doe', '20000', 'True', '01/01/2022')")
cursor.execute("INSERT or REPLACE into users (user_id, username, balance, subscription, datecreated) VALUES ('2', 'Jane Doe', '20000', 'True', '02/02/2022')")
cursor.execute("INSERT or REPLACE into users (user_id, username, balance, subscription, datecreated) VALUES ('3', 'Greg Gory','40000', 'True', '03/03/2022')")
cursor.execute("INSERT or REPLACE into users (user_id, username, balance, subscription, datecreated) VALUES ('4', 'Muffin McDean', '15000', 'True', '04/04/2022')")

cursor.execute("INSERT or REPLACE into orders (orders_id, stock, price, quantity, datecreated) VALUES ('1', 'XYZCorp','300', '100', '12/12/2021')")

connection.commit()