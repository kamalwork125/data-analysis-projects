# 📊 Data Analysis Projects

Welcome to my Data Analysis portfolio! This repository contains real-world projects that demonstrate my ability to work with data, clean it, analyze patterns, and present insights using Python and visualization libraries.

---

## 📁 Projects Included

### 1. 🔍 Sales Dashboard Analysis
- **Dataset:** SalesDataForDashboard.xlsx  
- **Objective:** Analyze regional sales performance and create a dashboard to visualize trends.
- **Tools Used:** Excel, Python, Pandas, Matplotlib

### 2. 📈 Student Performance Analyzer 
- **Dataset:** students_data.csv  
- **Objective:** Clean student data, calculate averages, and visualize marks by city.
- **Tools Used:** Pandas, Seaborn, Matplotlib

  
###3. 🛒 Customer Purchase Insights
Dataset: Customer_Purchase_Data.xlsx

Objective: Analyze customer demographics, purchasing behavior & segment-wise performance

Techniques: EDA, grouping, filtering

Tools: Pandas, Seaborn, Matplotlib


###4. 📆 Monthly Sales Performance Tracker
Dataset: Monthly Sales Performance Tracker.xlsx
Objective: Month-wise product category performance, revenue trends & top-selling items
Techniques: Pivot tables, time-series visualization
Tools: Pandas, Excel, Matplotlib


###5 📊 Netflix Data Analysis Project
 1️⃣ How has the number of Netflix releases changed over the years?
- ✅ Line chart showing year-wise growth in releases.
 2️⃣ What is the ratio of Movies vs TV Shows on Netflix?
- ✅ Bar chart showing count comparison.
- ✅ Pie chart showing percentage ratio.
 3️⃣ Which are the top 10 countries producing Netflix content?
- ✅ Bar chart showing top-producing countries based on content count.
  4️⃣ What are the top 10 most common genres on Netflix?
- ✅ Bar chart showing most frequent genres from the `listed_in` column.
 5️⃣ What is the distribution of movie durations?
- ✅ Histogram showing how long most Netflix movies are (in minutes).
- 
- ###6# 🛒 E-commerce Sales Analysis (Python Project)
 📌 Project Overview
This project analyzes a simulated E-commerce sales dataset using Python. The dataset includes customer purchases, product details, delivery performance, and ratings. The goal is to uncover business insights such as top-performing products, delivery trends, customer satisfaction, and city-wise revenue
## 🧹 Data Cleaning
- Filled nulls in numeric columns (`Price Each`, `Customer Rating`) with mean/median.
- Filled missing product names with `"Unknown Product"`.
- Converted `Order Date` to datetime.
- Added a new column: `Sales = Quantity Ordered × Price Each`.
 📊 Key Analysis Performed
 ✅ 1. Top-Selling Product Categories
- Found categories with the highest total revenue using groupby and barplot.
 ✅ 2. Average Delivery Time by City
- Calculated average delivery days for each city to evaluate logistics performance.
 ✅ 3. Top 5 Rated Products
- Identified products with highest average customer ratings.
 ✅ 4. City-wise Revenue
- Found which cities brought in the most revenue.
 ✅ 5. Correlation Analysis
- Checked relationship between `Quantity Ordered` and `Customer Rating`.
 📈 Tools Used
- **Python** (Pandas, NumPy)
- **Matplotlib** & **Seaborn** for data visualization
- **Jupyter Notebook** or VS Code for development
 📌 Sample Visuals

- Bar charts for revenue by city and category
- Horizontal bar plot for top-rated products
- Line plot for monthly sales
- Heatmap for correlation
 📘 Conclusion
- Most sales came from [Top Category] and [Top City].
- Delivery performance varied across cities.
- Customer satisfaction was higher for [Top Products].
- Null values were handled effectively before analysis.
 🧰 Tools & Technologies

- Python  
- Pandas  
- Numpy  
- Seaborn & Matplotlib  
- Jupyter Notebook  
- Excel / CSV  
- Git & GitHub
  
   📚 Library SQL Project
This is a beginner-level **SQL project** that simulates a simple Library Management System. It includes tables for members, books, and issued books. The project was executed using **SQLite**.
 🔧 Project Structure
 **library_project.sql** → Creates tables and inserts sample data.
**library_project_queries.txt** → Includes 5 SQL queries with their expected output
📄 Tables
1. **members**: Stores member details
2. **books**: Stores book information
3. **issued_books**: Tracks which member issued which book and when
 📊 SQL Queries Performed

1. Members who haven't returned books
2. Total number of books issued by each member
3. Book list with status (Issued/Available)
4. Books issued between specific dates
5. Count of unreturned books per member
🚀 How to Run
1. Install [SQLite](https://www.sqlite.org/download.html)
2. Open terminal and run:
    ```bash
    sqlite3 library.db
    .read library_project.sql
    ```
3. Run queries from `library_project_queries.txt` one by one
 ✨ Output Preview
Example:

```sql
SELECT m.name, COUNT(*) AS total_books_issued
FROM issued_books ib
JOIN members m ON ib.member_id = m.member_id
GROUP BY m.name;


 ##7🌆 City Happiness Analysis — Data Analytics Project

This project analyzes how different factors like Salary, AQI, Crime Rate, and City affect the overall Happiness Score.
You performed Cleaning → Analysis → Visualization → Machine Learning end-to-end.
📌 Project Overview

This project includes:
✔ Data Loading
✔ Handling Missing Values
✔ Outlier Detection (IQR Method)
✔ Correlation Analysis
✔ Exploratory Data Analysis (Seaborn + Plotly)
✔ Linear Regression Model
✔ Model Evaluation (R2, MAE, RMSE)
📁 Dataset
File: aa.csv
Contains columns like:
City
Salary
AQI
Crime_Rate
Happiness
and more…

🔧 Technologies Used
Python
Pandas
NumPy
Seaborn
Matplotlib
Plotly
Scikit-Learn

🧹 Data Cleaning Steps
Removed/filled missing values
Converted categorical columns using Label Encoding
Identified outliers using IQR
Generated descriptive statistics

📊 Visualizations Included
Correlation Heatmap
Pairplot
Scatter Plots
Box Plot
Interactive Plotly Visuals
Bubble Plot
Bar Chart
Interactive Scatter

🤖 Machine Learning Model
✔ Algorithm
Linear Regression
✔ Steps
Feature Scaling (StandardScaler)
Train-Test Split (80-20)
Model Training
Prediction
Model Evaluation
✔ Metrics
R² Score
MAE
RMSE
🏁 Results
Identified key factors affecting Happiness
Built a regression model
Visualized important relationships between features
<img width="1493" height="825" alt="Screenshot 2025-11-15 150738" src="https://github.com/user-attachments/assets/8cb8f307-aae2-454d-a736-20333367fdf7" />
<img width="1778" height="917" alt="Screenshot 2025-11-15 150854" src="https://github.com/user-attachments/assets/11921b36-c976-4d1d-868a-ddeb1aed1e9c" />
<img width="1671" height="854" alt="Screenshot 2025-11-15 150910" src="https://github.com/user-attachments/assets/441e913a-a2e0-41a1-9cc8-521f1e1cf1c6" />
<img width="941" height="777" alt="Screenshot 2025-11-15 150921" src="https://github.com/user-attachments/assets/4fb32cac-f4a5-4aca-83bd-a5f3a00dd261" />
<img width="944" height="775" alt="Screenshot 2025-11-15 150933" src="https://github.com/user-attachments/assets/7bcea865-d38d-4de2-8906-d9979d5fac17" />





## 👩‍💻 Author
**Kamaljot Kaur**  
_Data Analyst (Beginner level, portfolio project)_  





