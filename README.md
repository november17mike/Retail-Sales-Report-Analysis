# Retail-Sales-Report-Analysis
SQL Internship Project-Planner up until now, as to how can we approach this project.

# Objective- To provide a detailed analysis for an enterprise of their monthly retail sales using Python (Frontend) and SQL (backend).

1. First making an ER Diagram will help us understand what all tables to include and what all to drop which are not connected (not having required relations)
2. For ER diagram I have used dbdiagram.io because we simply have to give it the tables we need and it will give us the ER Diagram we need.
3. After making an idea from ER Diagram, we proceed to make a database and finally go on and make the tables we need.
4. We project some example data into it and then use Python to generate Test Data into the SQL.
5. We will connect SQL to Python using Connector.
6. We Use Faker- Library to generate the fake entries because mannually feeding 1000+ entries will be too much!!

# I have used 6 tables by far for the ER Diagram, namely:
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

Relationships:
1 Customer → many Orders
1 Order → many Order_Items
1 Product can appear in many Order_Items
1 Order → 1 Payment
1 Product → 1 Vendor
1 Vendor → many Products

