import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mirac23",
    database = "mydatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")

# mycursor.execute("SHOW DATABASES")

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), adress VARCHAR(255))")

# print(mydb)

# for i in mycursor:
#     print(i)