# Data Cleaning & Visualization Project
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("raw_customer_purchases.csv")
print("Shape:", df.shape)
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

# Missing values
for col in ["Age", "Monthly_Income", "Purchase_Amount", "Rating"]:
    df[col] = df[col].fillna(df[col].median())

# Remove duplicates
df = df.drop_duplicates()

# IQR outlier capping
def iqr_cap(series):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return series.clip(lower, upper)

df["Age"] = iqr_cap(df["Age"])
df["Purchase_Amount"] = iqr_cap(df["Purchase_Amount"])

# Visualizations
sns.set_theme(style="whitegrid")

plt.figure()
sns.barplot(data=df, x="Product_Category", y="Purchase_Amount", estimator="mean")
plt.title("Average Purchase Amount by Product Category")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

plt.figure()
sns.countplot(data=df, x="City")
plt.title("Customer Count by City")
plt.tight_layout()
plt.show()

plt.figure()
sns.histplot(data=df, x="Age", kde=True)
plt.title("Age Distribution")
plt.tight_layout()
plt.show()

plt.figure()
sns.scatterplot(data=df, x="Monthly_Income", y="Purchase_Amount", hue="Gender")
plt.title("Income vs Purchase Amount")
plt.tight_layout()
plt.show()

print(df.describe(include="all"))
