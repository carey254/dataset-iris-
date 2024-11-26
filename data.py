import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Task 1: Load the Dataset
try:
    # Load the dataset (Iris dataset as an example)
    df = pd.read_csv('iris/iris.data', header=None)  # Use correct path and no header if the dataset has none
    df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']  # Assign column names
except FileNotFoundError:
    print("File not found. Ensure the dataset is in the working directory.")
    exit()

# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Explore the structure of the dataset
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
# Only fill missing values in numeric columns
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Confirm dataset is clean
print("\nDataset after handling missing values:")
print(df.isnull().sum())
