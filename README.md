# Global Electronics Data Analysis Project
Welcome to the Global Electronics Data Analysis project, a comprehensive data-driven analysis for a leading electronics retailer. This project explores customer, sales, product, and store data to uncover key insights and support strategic decision-making. Utilizing Python, SQL, Power BI, and Jupyter Notebook, we analyze data trends and make actionable recommendations for growth.

# Project Overview
Global Electronics provided datasets containing customer, product, sales, store, and currency exchange information. Through this project, we aimed to:

Analyze customer behavior, product popularity, and store performance.
Identify trends, patterns, and potential areas for optimization.
Provide recommendations to enhance customer satisfaction, improve marketing, and optimize inventory.

# Table of Contents 
Project Overview 
Data Processing 
Exploratory Data Analysis (EDA)
SQL Queries for Business Use Cases
Power BI Dashboard
Insights and Recommendations
Technologies Used
How to Run This Project
# Data Processing
Data cleaning and transformation were crucial for reliable analysis. Key data processing steps included:

Handling Missing Values: Managed missing data through imputation and removal, ensuring data completeness.
Data Normalization: Standardized columns and converted data types, such as dates to datetime format.
Outlier Detection: Identified and removed outliers in key columns, such as price and sales, using Tukey's method.
Merging Datasets: Joined multiple datasets (sales, customers, products, stores, and exchange rates) for comprehensive analysis.
# Exploratory Data Analysis (EDA)
In the EDA phase, we visualized data trends and distribution patterns using Matplotlib and Seaborn. Key visualizations included:

Customer Spend Distribution (Violin Plot): Explores the distribution of spending across customer segments.
Sales by Region Over Time (Stacked Area Chart): Reveals regional sales trends and seasonality.
Product Category Sales (Circular Bar Plot): Shows the sales distribution across product categories.
Seasonality of Sales: Analyzes sales patterns by month or quarter to understand demand cycles.
These plots helped us gain insights into high-demand products, popular regions, customer spending patterns, and seasonal trends.

# SQL Queries for Business Use Cases
To further analyze data, we used SQL queries to answer business questions. Key queries include:

# Customer Purchase Distribution:

sql
SELECT CustomerKey, COUNT(OrderNumber) AS PurchaseCount FROM sales_data GROUP BY CustomerKey;
Use Case: Understand customer purchasing patterns.
# Top-Selling Products:

sql
SELECT ProductKey, SUM(Quantity) AS TotalQuantity FROM sales_data GROUP BY ProductKey ORDER BY TotalQuantity DESC;
Use Case: Identify most popular products.
# Sales by Region:

sql
SELECT Region, SUM(SalesAmount) FROM sales_data GROUP BY Region;
Use Case: Compare sales performance across regions.

# Discounted vs. Non-Discounted Sales Performance:

sql
SELECT DiscountApplied, SUM(SalesAmount) FROM sales_data GROUP BY DiscountApplied;
Use Case: Analyze how discounts impact sales.
# Store Performance:

sql
SELECT StoreKey, SUM(SalesAmount) AS TotalSales FROM sales_data GROUP BY StoreKey;
Use Case: Assess each store’s contribution to total sales.

# Power BI Dashboard
A Power BI dashboard was developed to present key findings. The dashboard includes visuals like bar charts, line graphs, and pie charts to illustrate trends in customer behavior, product performance, regional sales, and more.

# Insights and Recommendations
Key insights and recommendations for Global Electronics include:

Product Popularity: Computers are high-demand items. Recommendation: Invest in stock and marketing for top-selling categories.
Customer Demographics: Younger customers (ages 20-35) contribute to a large share of sales. Recommendation: Target marketing efforts for this demographic.
Regional Demand: High sales in urban regions suggest stronger demand. Recommendation: Consider expansion in urban areas and refine inventory management for regional demand.
Seasonal Trends: Significant sales spikes in Q4 suggest holiday demand. Recommendation: Increase inventory and promotions during this season.
# Technologies Used
Python: Data processing and visualization
SQL: Data querying and analysis
Power BI: Dashboard creation for data presentation
Jupyter Notebook: Code development and documentation
Matplotlib & Seaborn: Visualization libraries for EDA
# How to Run This Project
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/Global-Electronics-Data-Analysis.git
cd Global-Electronics-Data-Analysis
Set Up the Environment:

Install required Python packages:
bash
Copy code
pip install -r requirements.txt
Run Jupyter Notebooks:

Start Jupyter Notebook:
bash
Copy code
jupyter notebook
Open and run the data processing, EDA, and SQL query notebooks.
Power BI Dashboard:

Open the provided Power BI file (Global_Electronics_Dashboard.pbix) in Power BI to view the dashboard.
# Conclusion
This project leverages advanced data analysis and visualization to uncover insights and recommendations for Global Electronics. By analyzing customer behavior, sales trends, and product performance, the company can enhance its strategies to drive growth and customer satisfaction.

Feel free to explore and contribute to this project. Your feedback and suggestions are welcome!
