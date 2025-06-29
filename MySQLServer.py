import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # الاتصال بخادم MySQL (بدون تحديد قاعدة بيانات)
        connection = mysql.connector.connect(
            host='localhost',
            user='randa',
            password='1995'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
