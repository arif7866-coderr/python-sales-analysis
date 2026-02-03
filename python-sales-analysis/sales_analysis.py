import pandas as pd
import matplotlib.pyplot as plt

# Load data
data_path = "data/sales_data.csv"
df = pd.read_csv(data_path)

# Inspect data
print(df.head())
print(df.info())

# Convert date column
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Check missing values
print(df.isnull().sum())

# ===============================
# Sales by Region
# ===============================
sales_by_region = df.groupby('Region')['Sales'].sum()
print(sales_by_region)

plt.figure(figsize=(6,4))
plt.bar(sales_by_region.index, sales_by_region.values) #type: ignore
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.title("Sales by Region")
plt.savefig("output/sales_by_region.png")
plt.show()

# ===============================
# Monthly Sales Trend
# ===============================
df['Month'] = df['Order_Date'].dt.to_period('M') #type: ignore
monthly_sales = df.groupby('Month')['Sales'].sum()
print(monthly_sales)

plt.figure(figsize=(6,4))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker='o') #type: ignore
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales Trend")
plt.savefig("output/monthly_sales_trend.png")
plt.show()

# ===============================
# Top 5 Products by Sales
# ===============================

top_products = (
    df.groupby('Product')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

plt.figure(figsize=(6, 4))
top_products.plot(kind='bar')
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.title("Top 5 Products by Sales")
plt.tight_layout()
plt.savefig("output/top_products.png")
plt.show()