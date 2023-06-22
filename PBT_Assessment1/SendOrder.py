from dbm import _Database
import mysql.connector
import typer 
import os
from datetime import datetime

app = typer.Typer()

mydb = mysql.connector.connect(
 host="127.0.0.1",
 port = "3307",
 user="root",
 passwd="Banana1234"
)

stock_name = ""

def initDB():
    mycursor = mydb.cursor()
    mycursor.execute('USE MarketExchange.db')

def displayMainMenu():
    print(' — — — — MENU — — — -')
    print(' 1. Register User')
    print(' 2. order')
    print (' 3. exit')
    print(' — — — — — — — — — — ')
    
def registerUser():
   mycursor = mydb.cursor()
   print(' — — — User Registration — — — \n')
   username = input('Enter user name : ')
   balance = int(input('Enter user desired balance : '))
   sql = 'INSERT INTO "users" ("username","balance") VALUES ([],[])'
   val = (username, balance)
   mycursor.execute(sql,val)
   mydb.commit()
   print('Welcome new user \n')
   exit()

def order():
    mycursor = mydb.cursor()
    user_name = input('Enter your username:')
    stock_name = input('Enter stockname:')
    price: int(input('Enter the price you wish you purchase'))
    quantity = int(input('How many would you like to purchase'))
    order_type = bool(input('Are you buying or selling? 0 = sell, 1= buy'))
    sql = 'INSERT INTO "orders" ("user_name","stock_name", "price", "quantity", "order_type") VALUES ((%s), (%s), (%s), (%s), (%s))'
    val = (user_name, stock_name, price, quantity, order_type)
    mycursor.execute(sql,val)
    mydb.commit()
    print('Your Order has been sent \n')
    exit()

def exit():
    n = int(input(" Press 5 if you wish to exit: "))
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
      registerUser()
   elif n == 2:
      os.system('cls')
      order()
   elif n == 3:
      os.system('cls')
      print(' Have a great day!')
   else:
      os.system('cls')
      run()

if __name__ == "__main__":
    typer.run(main)




