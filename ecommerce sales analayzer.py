import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate
df=pd.read_csv("ecommerce.csv")
print(tabulate(df,headers='keys',tablefmt='psql'))
print("NULL VALUES:",df.isnull().sum())
df['Price Each'] = df['Price Each'].fillna(df['Price Each'].median())
df['Delivery Time (Days)'] = df['Delivery Time (Days)'].fillna(df['Delivery Time (Days)'].mean())
df['Customer Rating'] = df['Customer Rating'].fillna(df['Customer Rating'].mean())
df['Product Name'] = df['Product Name'].fillna('Unknown Product')
print("✅ Nulls after filling:\n", df.isnull().sum())
df['Sales'] = df['Quantity Ordered'] * df['Price Each']
print(df[['Product Name', 'Quantity Ordered', 'Price Each', 'Sales']].head())
#1)Which Product Category Generated the Most Revenue?
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print(category_sales)

# Plotting
category_sales.plot(kind='bar', title='Total Sales by Category', ylabel='Revenue', xlabel='Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#2)What is the Average Delivery Time in Each City?
avg_delivery = df.groupby('City')['Delivery Time (Days)'].mean().sort_values(ascending=False)
print(avg_delivery)
plt.figure(figsize=(10, 5))
sns.barplot(x=avg_delivery.index, y=avg_delivery.values)
plt.title("average delivery time")
plt.xlabel("city")
plt.ylabel("Average Delivery Days")
plt.grid(True)
plt.tight_layout()
plt.show()
#3)Top 5 Products by Average Customer Rating?
avg_rating = df.groupby('Product Name')['Customer Rating'].mean().sort_values(ascending=False).head(5)
print(avg_rating)
plt.figure(figsize=(10, 5))
sns.barplot(x=avg_rating.values, y=avg_rating.index)
plt.title("average product ratings")
plt.xlabel("ratings")
plt.ylabel("product")
plt.grid(True)
plt.tight_layout()
plt.show()
#4)Correlation Between Quantity Ordered and Customer Rating
correlation = df[['Quantity Ordered', 'Customer Rating']].corr()
print("Correlation:\n", correlation)
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
#5)Which City Generated the Highest Total Sales?
# Group by City and sum the total sales
city_sales = df.groupby('City')['Sales'].sum().sort_values(ascending=False)
print(city_sales)
plt.figure(figsize=(10, 5))
sns.barplot(x=city_sales.index, y=city_sales.values)
plt.title("Total Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales (₹)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


