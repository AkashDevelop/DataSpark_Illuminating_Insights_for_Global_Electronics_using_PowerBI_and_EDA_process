# Global Electronics Data Analysis Project 📊

Welcome to the Global Electronics Data Analysis project! This project provides in-depth data-driven insights for a major electronics retailer, analyzing customer, sales, product, and store data to help inform strategic decisions.

![Data_Analysis_Project](https://img.shields.io/badge/INTRODUCTION-blue)  
This project leverages Python, SQL, Power BI, and Jupyter Notebook to analyze data and provide actionable recommendations that support growth and enhance customer satisfaction.

## Project Overview 🚀
The Global Electronics Data Analysis project focuses on:
- **Customer Insights**: Understanding customer behavior and demographics
- **Sales Trends**: Identifying high-demand products and seasonality
- **Store Performance**: Evaluating regional and store-level performance
- **Recommendations**: Providing insights for inventory, marketing, and strategy optimization

## Table of Contents 📑
- [Project Overview](#project-overview-🚀)
- [Data Processing](#data-processing-🛠️)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda-📈)
- [SQL Queries for Business Use Cases](#sql-queries-for-business-use-cases-📊)
- [Power BI Dashboard](#power-bi-dashboard-📊)
- [Insights and Recommendations](#insights-and-recommendations-💡)
- [Technologies Used](#technologies-used-🖥️)
- [How to Run This Project](#how-to-run-this-project-⚙️)

## Data Processing 🛠️
The data processing steps included:
1. **Handling Missing Values**: Managing incomplete data through imputation and removal.
2. **Data Normalization**: Standardizing columns and data types.
3. **Outlier Detection**: Removing outliers using Tukey's method.
4. **Merging Datasets**: Combining sales, customers, products, stores, and exchange rate data.

## Exploratory Data Analysis (EDA) 📈
EDA provided insights into trends and patterns with visualizations such as:
- **Customer Spend Distribution**: Violin plot showing spending across segments.
- **Sales by Region Over Time**: Stacked area chart to reveal trends and seasonality.
- **Product Category Sales**: Circular bar plot showing sales distribution by category.
- **Sales Seasonality**: Analyzing demand cycles by month or quarter.

## SQL Queries for Business Use Cases 📊
### Sample Queries:
- **Customer Purchase Distribution**:
   ```sql
   SELECT CustomerKey, COUNT(OrderNumber) AS PurchaseCount
   FROM sales_data
   GROUP BY CustomerKey;

- **Average Purchase Amount per Customer**:
   ```sql
   SELECT CustomerKey, AVG(TotalAmount) AS AveragePurchaseAmount
   FROM sales_data
   GROUP BY CustomerKey;

- **Power BI Dashboard 📊**:📊
A Power BI dashboard was created to present key insights, with visuals like bar charts, line graphs, and pie charts to illustrate:

Customer behavior and product performance
Regional sales trends
Store performance metrics

Insights and Recommendations 💡
Key recommendations include:

