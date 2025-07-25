# Project name- Online Retail Sales Analysis- Using Python and MySQL
(SQL Internship Project 1)

# Objective- To provide a detailed analysis for a retail enterprise on their monthly sales using Python (Frontend) and SQL (backend).
An integrated retail analytics dashboard built using Python (frontend) and MySQL (backend), using Faker for data generation and Matplotlib/Seaborn for data visualization. This dashboard provides insights into customer spending, sales trends, product demand, and city-wise revenue for a fictional retail enterprise operating across Odisha.

# Features:
1. Database-Driven Architecture using MySQL
2. Data Insertion using Faker for realistic simulation
3. Interactive Console Menu to choose reports
4. Data Visualizations using Matplotlib & Seaborn
5. Location Filter (default: Bhubaneswar, extendable to other cities)

## Tools & Technologies
1. Python-(Application frontend)
2. MySQL- (Backend database)
3. SQLAlchemy- (Python-MySQL connection)
4. Faker- (Generate realistic dummy data)
5. Pandas- (Data manipulation)
6. Matplotlib- (Data visualization)
7. Seaborn- (Statistical plots)

## Database (Tips):
1. First making an ER Diagram will help us understand what all tables to include and what all to drop which are not connected (not having required relations)
2. For ER diagram I have used dbdiagram.io because we simply have to give it the tables we need and it will give us the ER Diagram we need.
3. After making an idea from ER Diagram, we proceed to make a database and finally go on and make the tables we need.
4. We project some example data into it and then use Python to generate Test Data into the SQL.
5. We will connect SQL to Python using Connector.
6. We Use Faker- Library to generate the fake entries because mannually feeding 1000+ entries will be too much!!

  # Tables Used for ER Diagram:
    1. Customers:
      - customer_id 
      - name
      - email
      - phone
      - address
      - city
      - state
      - pincode
      - registered_on
    2. Products:
      - product_id 
      - name
      - brand
      - category
      - price
      - stock_quantity
      - vendor_id 
    3. Vendors:
      - vendor_id 
      - vendor_name
      - contact_email
      - gst_number
      - city
    4. Orders:
      - order_id 
      - customer_id 
      - order_date
      - total_amount
      - payment_id 
    5. Order_Items:
      - order_id 
      - product_id 
      - quantity
      - price_at_purchase
    6. Payments:
      - payment_id 
      - payment_mode     (UPI / COD) 
      - payment_status   (Paid / Failed / Pending)
      - payment_date
      
  # Relationships:
      1 Customer → many Orders
      1 Order → many Order_Items
      1 Product can appear in many Order_Items
      1 Order → 1 Payment
      1 Product → 1 Vendor
      1 Vendor → many Products

## Steps:
1. Clone this repository
2. Create MySQL database online_retail
3. Run the single Python script Online_Retail_frontend.py
4. View dashboard options:
  -> Top 10 Customers
  -> Monthly Sales Trends
  -> Product-wise Sales
  -> City-wise Sales
  -> Exit anytime with option 5

## Sample Reports:
1. Top 10 Customers
[Bar chart showing customer spending (Y-axis) vs names (X-axis)]
<img width="1000" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/961659c8-010e-42b7-9d89-49caab0259d3" />

2. Monthly Sales Trend
[Line plot of total monthly revenue]
<img width="1000" height="500" alt="Figure_2" src="https://github.com/user-attachments/assets/d9ffcbd5-b948-48a9-927f-04b9115b1bfb" />

3. Product-wise Distribution
[Pie chart of quantity sold per product]
<img width="700" height="700" alt="Figure_3" src="https://github.com/user-attachments/assets/986a373c-6ab5-41bb-8a3e-20a8ab80c0cb" />

4. Top 10 Cities by Revenue
[Bar chart showing cities sorted by sales]
<img width="1000" height="600" alt="Figure_4" src="https://github.com/user-attachments/assets/c77f0408-be5d-4741-a5c8-cc112da4a8e1" />

## Sample Menu:
![SharedScreenshot](https://github.com/user-attachments/assets/393c9f7b-4749-47d6-a6e5-8f7a48d8b883)

(All visualizations reflect current data from MySQL, dynamically updated on script execution each time.)
