import pandas as pd

data = [
    {"Date": "2025-01-10", "Region": "North", "Salesperson": "John Doe", "Product": "Laptop", "Units Sold": 5, "Unit Price": 900, "Total Revenue": 4500},
    {"Date": "2025-01-12", "Region": "South", "Salesperson": "Jane Smith", "Product": "Tablet", "Units Sold": 10, "Unit Price": 300, "Total Revenue": 3000},
    {"Date": "2025-01-13", "Region": "East", "Salesperson": "Bob Johnson", "Product": "Smartphone", "Units Sold": 7, "Unit Price": 500, "Total Revenue": 3500},
    {"Date": "2025-01-15", "Region": "West", "Salesperson": "Alice Lee", "Product": "Laptop", "Units Sold": 3, "Unit Price": 900, "Total Revenue": 2700},
    {"Date": "2025-01-17", "Region": "North", "Salesperson": "John Doe", "Product": "Smartphone", "Units Sold": 2, "Unit Price": 500, "Total Revenue": 1000},
    {"Date": "2025-01-20", "Region": "South", "Salesperson": "Jane Smith", "Product": "Laptop", "Units Sold": 4, "Unit Price": 900, "Total Revenue": 3600},
    {"Date": "2025-01-22", "Region": "East", "Salesperson": "Bob Johnson", "Product": "Tablet", "Units Sold": 8, "Unit Price": 300, "Total Revenue": 2400},
    {"Date": "2025-01-25", "Region": "West", "Salesperson": "Alice Lee", "Product": "Smartphone", "Units Sold": 5, "Unit Price": 500, "Total Revenue": 2500}
]

df = pd.DataFrame(data)

df["Date"] = pd.to_datetime(df["Date"])

print("📋 Data Preview:")
print(df.head())

print("\n$ Total Revenue by Salesperson $:")
print(df.groupby("Salesperson")["Total Revenue"].sum())

print("\n Units Sold by Region:")
print(df.groupby("Region")["Units Sold"].sum())

print("\n Most Sold Product:")
print(df.groupby("Product")["Units Sold"].sum().sort_values(ascending=False))

daily_sales = df.groupby("Date")["Total Revenue"].sum()
print("\n Daily Sales Trend:")
print(daily_sales)
