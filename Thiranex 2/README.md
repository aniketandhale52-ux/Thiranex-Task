# 📊 Data Cleaning & Visualization Project

## 📌 Project Overview

This project focuses on cleaning, preprocessing, analyzing, and visualizing a raw customer purchase dataset using Python.

The main goal is to transform raw and inconsistent data into a clean, meaningful dataset and generate visual insights that can support data-driven decision-making.

## 🎯 Objectives

* Handle missing values
* Identify and remove duplicate records
* Detect and handle outliers
* Perform data preprocessing
* Analyze customer purchase behavior
* Create meaningful visualizations
* Extract useful insights from the dataset
* Present findings through data storytelling

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data manipulation and preprocessing
* **NumPy** – Numerical operations
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical visualization

## 📂 Project Structure

```text
Data-Cleaning-Visualization/
│
├── raw_customer_purchases.csv
├── cleaned_customer_purchases.csv
├── cleaning_summary.csv
├── data_cleaning_visualization.py
├── Project_Report.txt
├── requirements.txt
│
├── 01_avg_purchase_by_category.png
├── 02_total_purchase_by_city.png
├── 03_age_distribution.png
└── 04_income_vs_purchase.png
```

## 🧹 Data Cleaning Process

The following preprocessing techniques were applied:

### 1. Missing Values

Missing numerical values were identified and replaced using the **median value** of the respective columns.

### 2. Duplicate Records

Duplicate records were detected and removed to maintain data quality.

### 3. Outlier Detection

The **Interquartile Range (IQR)** method was used to identify extreme values.

Outliers in important numerical columns such as:

* Age
* Purchase Amount

were handled using IQR-based capping.

## 📊 Data Visualization

The project generates the following visualizations:

### Average Purchase Amount by Product Category

Shows the average amount spent by customers across different product categories.

### Total Purchase Amount by City

Shows which cities contribute the highest total purchase amount.

### Age Distribution

Displays the distribution of customer ages after data cleaning.

### Income vs Purchase Amount

Shows the relationship between monthly income and customer purchase amount.

## 🔍 Key Insights

* Electronics customers show relatively high purchase amounts.
* Major cities contribute significantly to overall purchases.
* Most customers belong to a normal working-age group after outlier treatment.
* Monthly income shows a positive relationship with purchase amount, although the relationship is not perfect.
* Data cleaning improves the reliability of analysis and visualization.

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the Project

```bash
cd Data-Cleaning-Visualization
```

### Step 3: Install Dependencies

```bash
py -m pip install -r requirements.txt
```

### Step 4: Run the Python Program

```bash
py data_cleaning_visualization.py
```

The generated visualizations will be displayed using Matplotlib.

## 📈 Expected Outcome

This project demonstrates the complete basic workflow of:

**Raw Data → Data Cleaning → Preprocessing → Analysis → Visualization → Insights**

It provides practical experience in data preprocessing, exploratory data analysis, visualization, and data storytelling.

## 🚀 Future Improvements

* Build an interactive Streamlit dashboard
* Add more advanced statistical analysis
* Implement automated outlier detection
* Add correlation heatmaps
* Add interactive Plotly charts
* Deploy the dashboard online
* Use a larger real-world dataset

## 👨‍💻 Author

**Aniket Andhale**

B.Tech – Artificial Intelligence & Data Science

## ⭐ Conclusion

This project demonstrates how raw data can be transformed into meaningful information using Python-based data cleaning and visualization techniques. It provides a strong foundation for further Data Science and Machine Learning projects.
