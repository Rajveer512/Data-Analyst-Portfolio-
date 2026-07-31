import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("superstore.csv")
print(df.head())
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())
print("\n--- SALES SUMMARY ---")

print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())
print("Total Quantity Sold:", df["Quantity"].sum())

print("\nSales by Category:")
print(df.groupby("Category")["Sales"].sum())
category_sales = df.groupby("Category")["Sales"].sum()

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sales_by_category.png", dpi=300, bbox_inches="tight")
plt.show()