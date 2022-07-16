import mysql.connector as mc
from mysql.connector import Error

def BDconnexion(Server,User,Password,DataBase):
    try:
        conn = mc.connect(host=Server, user=User, password=Password, database=DataBase)
        return conn
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if conn.is_connected():
            conn.close()
            print("MySQL connection is closed")
