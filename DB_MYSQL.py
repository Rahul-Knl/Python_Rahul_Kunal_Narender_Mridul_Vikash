import mysql.connector

# Connect to the MySQL server
db = mysql.connector.connect(
    host="localhost",
    user="test_local",
    password="local"
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Create a new database
cursor.execute("CREATE DATABASE python_test")

print("Database 'python_test' created successfully.")

# Close the cursor and database connection
cursor.close()
db.close()
