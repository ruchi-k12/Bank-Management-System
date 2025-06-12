from register import * 
from bank import *

status=False

print("Welcome to Ruchita Banking Project")

while True:
    try:
        register=int(input("1.SignUp:\n" "2.SignIn:"))
        
        if register == 1 or register == 2:
            if register == 1:
                SignUp()
            if register == 2:
                user=SignIn() 
                status=True
                break   
        else:
            print("please Enter Valid Input From Options")

    except ValueError:
         print("Invalid Input Try Again with Numbers")   

account_no = db_query(f"SELECT account_no From customers Where username = '{user}';")

while status:
    print(f"Welcome {user.capitalize()} choose Your Banking Sevices \n")

    try:
        facility = int(input("1.Balance Enquiry:\n" 
                             "2.Cash Deposite:\n"
                             "3.Cash Withdraw:\n"
                             "4.Fund Transfer:\n"
                             ))
        
        if facility >= 1 and facility <= 4:
            if facility == 1:
                 bobj=Bank(user,account_no[0][0])
                 bobj.balanceenquiry()
                                
            elif facility == 2:
                while True:
                    try:
                      amount = int(input("Enter Amount to Deposite:"))
                      bobj=Bank(user,account_no[0][0])
                      bobj.deposit(amount)
                      mydb.commit()
                      status = False
                    except ValueError:
                        print("Enter valid Input ie.Number")
                        continue

            elif facility == 3:
                while True:
                    try:
                      amount = int(input("Enter Amount to Withdraw:"))
                      bobj=Bank(user,account_no[0][0])
                      bobj.withdraw(amount)
                      mydb.commit()
                      status = False
                    except ValueError:
                        print("Enter Valid Input ie.Number")
                        continue
                
            elif facility == 4:
                while True:
                    try:
                        receive=(input("Enter Receiver Account Number:"))
                        amount=int(input("Enter Money to transfer:"))
                        
                        bobj=Bank(user,account_no[0][0])
                        bobj.fundtransfer(receive,amount)  
                        mydb.commit()
                        status = False
                    except ValueError:
                        print("Enter valid input ie.Number")    
                        continue
                    
                 
        else:
            print("please Enter Valid Input From Options")
            continue

    except ValueError:
         print("Invalid Input Try Again with Numbers")  
         continue 