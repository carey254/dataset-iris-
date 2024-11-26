# Line Chart: Trends over time
# Assuming a time column exists in the dataset, use a time-series dataset for this
import sns
from matplotlib import pyplot as plt

from PANDAS.data import df

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='sepal_length', y='petal_length', hue='species')
plt.title("Trend of Petal Length vs. Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.legend(title="Species")
plt.show()

# Bar Chart: Comparison across categories
plt.figure(figsize=(8, 6))
sns.barplot(x=grouped_data.index, y=grouped_data.values, palette='viridis')
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length")
plt.show()

# Histogram: Distribution of a numerical column
plt.figure(figsize=(8, 6))
sns.histplot(df['sepal_width'], kde=True, bins=20, color='blue')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot: Relationship between two numerical columns
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='sepal_length', y='petal_length', hue='species', style='species', palette='dark')
plt.title("Scatter Plot of Sepal Length vs. Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.legend(title="Species")
plt.show()
