#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (without selecting a database)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""  # Replace with your MySQL password if you have one
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print("Error: Could not connect to MySQL server.")
        print(f"{e}")

    finally:
        try:
            if cursor:
                cursor.close()
        except:
            pass
        try:
            if connection and connection.is_connected():
                connection.close()
                print("MySQL connection is closed.")
        except:
            pass

if __name__ == "__main__":
    create_database()
