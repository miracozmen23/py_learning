import mysql.connector

def insertProducts (name,price,imageUrl,description):
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mirac23",
    database = "node-app"
)
    mycursor = mydb.cursor()
    
    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,imageUrl,description)
    mycursor.execute(sql,values)
    
    try:
        mydb.commit()
        print(f"{mycursor.rowcount} tane kayıt eklendi")
        print(f"Son eklenen kaydın id'si: {mycursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata",err)
    finally:
        mydb.close()
        print("Database bağlantısı kapatıldı")

name = input("Ürün adı: ")
price = float(input("Ürün Fiyatı: "))
imageUrl = input("Ürün resminin url'si: ")
description = input("Ürün açıklaması: ")

insertProducts(name,price,imageUrl,description)