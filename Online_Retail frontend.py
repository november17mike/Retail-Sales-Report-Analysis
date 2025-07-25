
import mysql.connector
from faker import Faker
import random
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# ---------- 0. Welcome Display ----------
print("Welcome to Mohanty Solutions Ltd!")

# ---------- 1. Configuration ----------
HOST = "localhost"
USER = "root"
PASSWORD = "Nkm@5120800"  
DATABASE = "online_retail"

# ---------- 2. Connecting & Creating Database ----------
conn = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD
)
cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS online_retail")
cursor.execute("CREATE DATABASE online_retail")
cursor.execute("USE online_retail")

# ---------- 3. Creating Tables ----------
cursor.execute("""
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50)
)
""")

cursor.execute("""
CREATE TABLE Products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100),
    category VARCHAR(50),
    unit_price DECIMAL(10,2)
)
""")

cursor.execute("""
CREATE TABLE Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
)
""")

cursor.execute("""
CREATE TABLE Order_Items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
)
""")
print("Your report is processing---- Please wait....")

# ---------- 4. Feeding Data ----------
fake = Faker()

# Manual Customers input
manual_customers = [
    ('Aditi Sharma', 'aditi@gmail.com', 'Sambalpur'),
    ('Rahul Mehra', 'rahul@gmail.com', "Puri"),
    ('Neha Verma', 'neha@gmail.com', 'Bhubaneswar')
]
for customer in manual_customers:
    cursor.execute("INSERT INTO Customers (customer_name, email, city) VALUES (%s, %s, %s)", customer)

# Manual Products
manual_products = [
    ("Laptop", "Electronics", 55000),
    ("Smartphone", "Electronics", 25000),
    ("Headphones", "Accessories", 1500),
    ("Keyboard", "Accessories", 1000),
    ("Monitor", "Electronics", 8000),
    ("Mouse", "Accessories", 500),
    ("Tablet", "Electronics", 22000),
    ("Printer", "Electronics", 7000),
    ("Camera", "Electronics", 30000),
    ("Router", "Networking", 2000)
]
for product in manual_products:
    cursor.execute("INSERT INTO Products (product_name, category, unit_price) VALUES (%s, %s, %s)", product)

# Faker Customers
for _ in range(117):
    name = fake.name()
    email = fake.email()
    city = fake.city()
    cursor.execute("INSERT INTO Customers (customer_name, email, city) VALUES (%s, %s, %s)", (name, email, city))

# Orders and Order Items
for _ in range(1000):
    customer_id = random.randint(1, 100)
    order_date = fake.date_between(start_date='-30d', end_date='today')
    cursor.execute("INSERT INTO Orders (customer_id, order_date) VALUES (%s, %s)", (customer_id, order_date))
    order_id = cursor.lastrowid

    for _ in range(random.randint(1, 3)):
        product_id = random.randint(1, 5)
        quantity = random.randint(1, 5)
        cursor.execute("INSERT INTO Order_Items (order_id, product_id, quantity) VALUES (%s, %s, %s)", (order_id, product_id, quantity))

conn.commit()
print("Processing Over---Go!")

# ---------- 5. Reporting and Visualization ----------
conn = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=DATABASE
)
engine = create_engine(f"mysql+pymysql://root:Nkm%405120800@localhost/online_retail")

def top_10_customers():
    query = """
    SELECT 
        c.customer_name,
        SUM(oi.quantity * p.unit_price) AS total_spent
    FROM Customers c
    JOIN Orders o ON c.customer_id = o.customer_id
    JOIN Order_Items oi ON o.order_id = oi.order_id
    JOIN Products p ON oi.product_id = p.product_id
    GROUP BY c.customer_name
    ORDER BY total_spent DESC
    LIMIT 10;
    """
    df = pd.read_sql(query, engine)
    plt.figure(figsize=(10,6))
    plt.bar(df['customer_name'], df['total_spent'], color='yellow')
    plt.title("Top 10 Customers by Spending")
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Amount (₹)")
    plt.tight_layout()
    plt.show()

def sales_trend():
    query = """
    SELECT 
        DATE_FORMAT(o.order_date, '%%Y-%%m') AS month,
        SUM(oi.quantity * p.unit_price) AS total_sales
    FROM Orders o
    JOIN Order_Items oi ON o.order_id = oi.order_id
    JOIN Products p ON oi.product_id = p.product_id
    GROUP BY month
    ORDER BY month;
    """
    df = pd.read_sql(query, engine)
    plt.figure(figsize=(10,5))
    plt.plot(df['month'], df['total_sales'], marker='o', linestyle='-', color='maroon')
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales (₹)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def product_wise_sale():
    query = """
    SELECT 
        p.product_name,
        SUM(oi.quantity) AS total_quantity
    FROM Products p
    JOIN Order_Items oi ON p.product_id = oi.product_id
    GROUP BY p.product_name;
    """
    df = pd.read_sql(query, engine)
    plt.figure(figsize=(7,7))
    plt.pie(df['total_quantity'], labels=df['product_name'], autopct='%1.1f%%', startangle=140)
    plt.title("Sales Distribution by Product")
    plt.axis('equal')
    plt.show()

def top_10_cities():
    query = """
    SELECT 
        c.city,
        SUM(oi.quantity * p.unit_price) AS total_sales
    FROM Customers c
    JOIN Orders o ON c.customer_id = o.customer_id
    JOIN Order_Items oi ON o.order_id = oi.order_id
    JOIN Products p ON oi.product_id = p.product_id
    GROUP BY c.city
    ORDER BY total_sales DESC
    LIMIT 10;
    """
    df = pd.read_sql(query, engine)
    plt.figure(figsize=(10,6))
    plt.bar(df['city'], df['total_sales'], color='orange')
    plt.title("Top 10 Cities by Sales")
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Amount (₹)")
    plt.tight_layout()
    plt.show()

def main():
    while True:
        print("\nSales Data Dashboard - Choose what you'll want to see:")
        print("1. Top 10 Customers by Spending")
        print("2. Monthly Sales Trend")
        print("3. Product-wise Sales Distribution")
        print("4. Top 10 Cities by Sales")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            top_10_customers()
        elif choice == '2':
            sales_trend()
        elif choice == '3':
            product_wise_sale()
        elif choice == '4':
            top_10_cities()
        elif choice == '5':
            print("Exiting dashboard. Thank You!!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

conn.close()
print("Visual reports generated successfully.")
