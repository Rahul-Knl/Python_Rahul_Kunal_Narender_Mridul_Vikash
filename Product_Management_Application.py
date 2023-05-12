import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database_name"
)

cursor = db.cursor()

# Function to add a new product
def add_product(name, price, quantity):
    sql = "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)"
    values = (name, price, quantity)
    cursor.execute(sql, values)
    db.commit()
    print("Product added successfully.")

# Function to retrieve product details
def get_product(product_id):
    sql = "SELECT * FROM products WHERE id = %s"
    values = (product_id,)
    cursor.execute(sql, values)
    product = cursor.fetchone()
    if product:
        print("ID: {product[0]}\nName: {product[1]}\nPrice: {product[2]}\nQuantity: {product[3]}")
    else:
        print("Product not found.")

# Function to update product information
def update_product(product_id, name, price, quantity):
    sql = "UPDATE products SET name = %s, price = %s, quantity = %s WHERE id = %s"
    values = (name, price, quantity, product_id)
    cursor.execute(sql, values)
    db.commit()
    print("Product updated successfully.")

# Function to delete a product
def delete_product(product_id):
    sql = "DELETE FROM products WHERE id = %s"
    values = (product_id,)
    cursor.execute(sql, values)
    db.commit()
    print("Product deleted successfully.")

# Usage examples:
add_product("Apple", 1.99, 100)
get_product(1)
update_product(1, "Green Apple", 2.49, 80)
delete_product(1)

# Close the database connection
cursor.close()
db.close()
