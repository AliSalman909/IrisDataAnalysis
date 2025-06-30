import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data1 = pd.read_csv(r"C:\Users\Ali's HP\Desktop\Internship\task1\iris.csv")  #data is the dataframe for the csv file

print("Shape:", data1.shape)  # tells no of rows and cols
print("Columns:", data1.columns.tolist())  #lists the col names 
print(data1.head(10))  #top 10 values based on index val

#code to produce and display scatter plot
sns.scatterplot(data=data1, x='petal_length', y='petal_width', hue='species') #color on basis of species 
plt.title('Petal Length vs Petal Width by Species')
plt.show()

# create and show histogram 
sns.histplot(data=data1, x='sepal_length', kde=True)
plt.title('Distribution of Sepal Length')
plt.show()

# create and shiw box and whisker
sns.boxplot(data=data1, x='species', y='petal_length')
plt.title('Boxplot of Petal Length by Species')
plt.show()