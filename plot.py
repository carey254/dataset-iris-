import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('iris/iris.data', header=None)
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

plt.figure(figsize=(8, 6))
sns.barplot(x='species', y='petal_length', data=df, errorbar=None, palette='viridis', hue='species', dodge=False)
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length')
plt.show()

# 2. Histogram: Distribution of sepal length
plt.figure(figsize=(8, 6))
sns.histplot(df['sepal_length'], kde=True, bins=15, color='blue')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

# 3. Scatter Plot: Sepal length vs. Petal length
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df, palette='deep')
plt.title('Sepal Length vs. Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.legend(title='Species')
plt.show()

# 4. Line Chart: Simulated time-series of average petal width (for illustration)
time_series_data = df.groupby('species')['petal_width'].mean().reset_index()
time_series_data['time'] = [1, 2, 3]  # Simulated time points
plt.figure(figsize=(8, 6))
sns.lineplot(x='time', y='petal_width', marker='o', data=time_series_data, label='Petal Width')
plt.title('Simulated Time Series of Average Petal Width')
plt.xlabel('Time')
plt.ylabel('Average Petal Width')
plt.xticks(ticks=[1, 2, 3], labels=['Setosa', 'Versicolor', 'Virginica'])
plt.show()
