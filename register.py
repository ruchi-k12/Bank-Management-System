#User registration signin singup

from database import *
from customer import *
from bank import Bank
import random

def SignUp():
    username=input("Create Username:")
    temp = db_query (f"SELECT username FROM customers WHERE username = '{username}'; ")
    #print(temp)
    if temp:
        print("Username Already Exists")
        SignUp()

    else:
        print ("Username is Available please proceed")    
        password = input("Enter Your Password :")
        name=input("Enter Your name :")
        age=input("Enter Your age :")
        city=input("Enter Your city :")
        while True:
           account_no = random.randint(a=10000000 ,b=99999999)
           temp = db_query (f"SELECT  account_no FROM customers WHERE  account_no = '{ account_no}';")
           if temp:
               continue
           else:
                print("Your Account Number",account_no)
                break
    cobj = Customer(username, password,name,age,city,account_no)        
    cobj.createuser()
    bobj = Bank(username,account_no)
    bobj.create_tansaction_table()

def SignIn():
    username=input("Enter username:")
    temp = db_query (f"SELECT  username FROM customers WHERE  username = '{ username}';")
    if temp:
        while True:
          password=input(f"Welcome {username.capitalize()}  Enter password: ")
          temp = db_query (f"SELECT password FROM customers WHERE  username = '{username}';")
          #print(temp[0][0])
          if temp[0][0] == password:
              print("Sign IN Successfully ")
              return username
          else:
              print('Wrong password try again')    
              continue
    else:
        print("Enter correct username")
        SignIn()
