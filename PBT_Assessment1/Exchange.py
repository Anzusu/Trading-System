import sqlite3
import typer 
import os
from datetime import datetime

app = typer.Typer()

connection = sqlite3.connect('MarketExchange.db')
price = 30
quantity = 10

def displayMainMenu():
    print(' TRADES OF TODAY')
    print(' 1. order')
    print(' 2. transaction')
    print (' 3. exit')
    print(' — — — — — — — — — — ')

def order():
    sqlite3.connect('MarketExchange.db')
    user_name = input('Enter your username:')
    stock_name = input('Enter stockname:')
    price: int(input('Enter the price you wish you purchase'))
    quantity = int(input('How many would you like to purchase'))
    sql = 'INSERT INTO "orders" ("user_name","stock_name", "price", "quantity") VALUES ([],[])'
    val = (user_name, stock_name, price, quantity)
    connection.execute(sql, val)
    connection.commit()
    print('Your Order has been sent \n')
    exit()

def transaction():
    sqlite3.connect('MarketExchange.db')
    connection.execute("SELECT * FROM orders WHERE price = 30 quantity = 10")
    if price == 30 and quantity == 10:
        sql = 'DELETE FROM "orders" WHERE price = 30, quantity = 10'
        sql = 'INSERT INTO "trades" FROM "orders" ("user_name = username", "stock_name" = "stock_name", "price = stock_price", "quantity = stock_quantity")'
    elif price != 30 and quantity !=10:
        print('Your order is waiting to be matched up \n')
    exit()

def exit():
    n = int(input(' Press 5 if you wish to exit: '))
    if n == 5:
       os.system('cls')
       run()
    else:
       print("That is not an option, please try again")
       exit()    
    
def main():
   displayMainMenu()
   n = int(input("Enter option : "))
   if n == 1:
      os.system('cls') 
      order()
   elif n == 2:
      os.system('cls')
      transaction()
   elif n == 3:
      os.system('cls')
      print(' Have a great day!')
   else:
      os.system('cls')
      run()

if __name__ == "__main__":
    typer.run(main)
