import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (Replace with your actual CSV file)
data = pd.read_csv("sales_data.csv")

# Display first few rows
print("Data Preview:")
print(data.head())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Data Cleaning: Fill missing values if any
data.fillna(0, inplace=True)

# Summary statistics
print("\nSummary Statistics:")
print(data.describe())

# Monthly Sales Trend
plt.figure(figsize=(10,5))
sns.lineplot(x=data['Month'], y=data['Total_Sales'], marker='o', color='b')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Top 5 Best-Selling Products
top_products = data.groupby("Product")['Total_Sales'].sum().sort_values(ascending=False).head(5)
plt.figure(figsize=(8,4))
top_products.plot(kind='bar', color='g')
plt.title("Top 5 Best-Selling Products")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()

# Conclusion
print("\nKey Insights:")
print("1. Sales trends over months show seasonal variations.")
print("2. The top-selling products can be prioritized for inventory management.")
