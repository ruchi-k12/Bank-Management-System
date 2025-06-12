#Bank sevices
from database import *
import datetime

class Bank:

    def __init__(self,username,account_no):
        self.__username = username
        self.__account_no = account_no
        
        
    def create_tansaction_table(self):
        db_query (f"CREATE TABLE IF NOT EXISTS {self.__username}_transaction"
            f"(timedate varchar(30),"
            f"account_no INTEGER,"
            f"remarks VARCHAR(30),"
            f"amount INTEGER )")

    def balanceenquiry(self):
        temp=db_query(f"select balance from customers where username ='{self.__username}';")
        print(f"{self.__username} Balance is {temp[0][0]}");    

    def deposit(self,amount):
        temp=db_query(f"select balance from customers where username ='{self.__username}';")
        test = amount + temp[0][0]
        db_query(f"UPDATE customers SET balance ='{test}' where username ='{self.__username}';")
        self.balanceenquiry()
        db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                 f"'{datetime.datetime.now()}',"
                 f"'{self.__account_no}',"
                 f"'Amount Deposite',"
                 f"'{amount}'"
                 
                 f")")

        print(f"{self.__username} Amount is Successfully Deposited into your account{self.__account_no}")


    def withdraw(self,amount):
        temp=db_query(f"select balance from customers where username ='{self.__username}';")
        if amount > temp[0][0]:
            print("Insufficient balance please Deposite Money")
        else:
          test = temp[0][0] - amount
          db_query(f"UPDATE customers SET balance ='{test}' where username ='{self.__username}';")
          self.balanceenquiry()
          db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                 f"'{datetime.datetime.now()}',"
                 f"'{self.__account_no}',"
                 f"'Amount withdraw',"
                 f"'{amount}'"
                 
                 f")")

        print(f"{self.__username} Amount is Successfully Withdraw from your account{self.__account_no}")    

    def fundtransfer(self,receive,amount):
        temp=db_query(f"select balance from customers where username ='{self.__username}';")
        if amount > temp[0][0]:
            print("Insufficient Balance Please Deposite Money")
        else:
            temp2 = db_query(f"SELECT balance FROM customers WHERE account_no = '{receive}';")
            test1 =temp[0][0] - amount  
            test2 = amount + temp2[0][0]
            db_query(f"UPDATE customers SET balance ='{test1}' where username = '{self.__username}';")
            db_query(f"UPDATE customers SET balance ='{test2}' where account_no = '{receive}';")
            receiver_username = db_query(f"SELECT username FROM customers where account_no='{receive}';")
            self.balanceenquiry()
            db_query(f"INSERT INTO {receiver_username[0][0]}_transaction VALUES ("
                 f"'{datetime.datetime.now()}',"
                 f"'{self.__account_no}',"
                 f"'Fund Transfer from {self.__account_no}',"
                 f"'{amount}'"
                 
                 f")")
            db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                 f"'{datetime.datetime.now()}',"
                 f"'{self.__account_no}',"
                 f"'Fund Transfer -> {receive}',"
                 f"'{amount}'"
                 
                 f")")

        print(f"{self.__username} Amount is Successfully Transaction from your account {self.__account_no}")    

