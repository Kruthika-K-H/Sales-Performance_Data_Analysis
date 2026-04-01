import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load dataset
df = pd.read_csv("sales_modified.xlsx.csv", encoding='latin1')

# Step 2: Show basic info
print("First 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns)

# Step 3: Data Cleaning
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Step 4: Add new columns (IMPORTANT for project uniqueness)

# Profit Percentage
df['Profit_Percentage'] = (df['Profit'] / df['Sales']) * 100

# Discount Category
df['Discount_Level'] = df['Discount'].apply(
    lambda x: 'Low' if x < 0.2 else ('Medium' if x < 0.5 else 'High')
)

# Step 5: Analysis

# Total Sales by Category
category_sales = df.groupby('Category')['Sales'].sum()
print("\nSales by Category:")
print(category_sales)

# Top 5 Products
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Products:")
print(top_products)

# Step 6: Visualization

# Sales by Category (Bar Chart)
category_sales.plot(kind='bar', title='Sales by Category')
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.show()

# Profit by Discount Level (Bar Chart)
discount_profit = df.groupby('Discount_Level')['Profit'].sum()
discount_profit.plot(kind='bar', title='Profit by Discount Level')
plt.xlabel("Discount Level")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("profit_by_discount.png")
plt.show()

# Step 7: Save modified dataset
df.to_csv("final_dataset.csv", index=False)

print("\n✅ Process completed successfully!")