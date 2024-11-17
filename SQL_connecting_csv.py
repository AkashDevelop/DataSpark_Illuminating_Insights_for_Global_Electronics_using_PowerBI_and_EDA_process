import pandas as pd
import sqlite3
from tabulate import tabulate

# Step 1: Load the CSV file with dtype specification
file_path = "E:/DataSpark project/Data_cleaning_with_EDA.csv"

dtype_spec = {
    "Order Date": str,
    "Delivery Date": str,
    "CustomerKey": int,
    # Add more columns here if necessary
}

df = pd.read_csv(file_path, dtype=dtype_spec)

# Optional: Clean column names (remove any extra spaces)
df.columns = df.columns.str.strip()

# Step 2: Connect to SQLite database
con = sqlite3.connect("sales_data_analysis.db")
cur = con.cursor()

# Step 3: Check if table exists and create a new table if necessary
cur.execute("PRAGMA table_info(sales_data);")
columns = cur.fetchall()

# If the table already exists, drop it (optional)
if columns:
    print("Dropping existing 'sales_data' table.")
    cur.execute("DROP TABLE IF EXISTS sales_data")

# Create the table with correct schema based on the updated DataFrame
create_table_query = '''
    CREATE TABLE IF NOT EXISTS sales_data (
        "Order Number" INTEGER,
        "Line Item" INTEGER,
        "Order Date" TEXT,
        "Delivery Date" TEXT,
        "CustomerKey" INTEGER,
        "StoreKey" INTEGER,
        "ProductKey" INTEGER,
        "Quantity" INTEGER,
        "Currency Code" TEXT,
        "Gender" TEXT,
        "Name" TEXT,
        "City" TEXT,
        "State Code" TEXT,
        "State_x" TEXT,
        "Zip Code" REAL,
        "Country_x" TEXT,
        "Continent" TEXT,
        "Birthday" TEXT,
        "Product Name" TEXT,
        "Brand" TEXT,
        "Color" TEXT,
        "Unit Cost USD" REAL,
        "Unit Price USD" REAL,
        "SubcategoryKey" INTEGER,
        "Subcategory" TEXT,
        "CategoryKey" INTEGER,
        "Category" TEXT,
        "Country_y" TEXT,
        "State_y" TEXT,
        "Square Meters" REAL,
        "Open Date" TEXT,
        "Exchange" REAL,
        "Unit Price USD_original" REAL,
        "Sales Amount" REAL,
        "Age" INTEGER,
        "Month" INTEGER,
        "Cohort Month" TEXT,
        "Discounted" INTEGER,
        "Return" INTEGER
    );
'''

cur.execute(create_table_query)
con.commit()

# Step 4: Insert Data into the SQLite table
df.to_sql('sales_data', con, if_exists='append', index=False)

# Step 5: Commit changes and close connection
con.commit()
con.close()

print("Data successfully inserted into the sales_data table.")
