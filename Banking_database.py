import pymysql

# Connect to MySQL server
mydb = pymysql.connect(host="localhost", user="root", password="root")

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Create a new database named "Banking" if it does not already exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS Banking")

# Reconnect to the MySQL server with the newly created database
mydb = pymysql.connect(host="localhost", user="root", password="root", database="Banking")

# Create a cursor object for the newly connected database
mycursor = mydb.cursor()

# Commit changes to the database (in this case, creating the new database)
mydb.commit()


