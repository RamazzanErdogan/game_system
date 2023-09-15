import mysql.connector

mydb=mysql.connector.connect(
user="root",
password="mysql123",
host="localhost",
database="kullanıcı_bilgileri"
)
def get_kullanıcıadı():
    mybd_select=mydb.cursor()
    mybd_select.execute("SELECT kullanıcıadı From kullanıcılar")
    result=mybd_select.fetchall()
    mydb.commit()
    return result
       
def get_parola():
    mybd_select=mydb.cursor()
    mybd_select.execute("SELECT parola From kullanıcılar")
    result=mybd_select.fetchall()
    return result
