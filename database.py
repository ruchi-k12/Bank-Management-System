import mysql.connector as sql 

mydb=sql.connect(

    host='localhost',
    user='root',
    password='root',
    database='bank1',
    port='3306'
)

cursor=mydb.cursor()

def db_query(str):
     cursor.execute(str)
     result = cursor.fetchall()
     return result

def createcustomertable():
 cursor.execute('''
               create table if not exists customers
               (username varchar(20),
                password varchar(20),
                name varchar(20),
                age integer,
                city varchar(20),
                balance integer NOT NULL,
                account_no integer,
                status boolean )

''')

mydb.commit()

if __name__ == "__main__":
  createcustomertable()