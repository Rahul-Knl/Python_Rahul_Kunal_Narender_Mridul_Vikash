import mysql.connector

# Connect to the MySQL server
db = mysql.connector.connect(
    host="localhost",
    user="python_test",
    password="test123"
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Create a new database
cursor.execute("CREATE DATABASE test")

print("Database 'test' created successfully.")

# Close the cursor and database connection
cursor.close()
db.close()
