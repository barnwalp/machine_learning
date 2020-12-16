import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
from matplotlib import interactive
import os
import seaborn as sns


interactive(True)
pd.set_option('max_columns', None)
file_path = os.path.join(os.getcwd(), 'datasets', 'kaggle_dataset')
iris_path = os.path.join(file_path, 'iris.csv')
iris_data = pd.read_csv(iris_path, index_col='Id')

# kde=False will not plot kernel density estimate plot
sns.distplot(a=iris_data['Petal Length (cm)'], kde=False)

# Plotting kdeplot
sns.kdeplot(data=iris_data['Petal Length (cm)'], shade=True)

# 2 KDE Plots
sns.jointplot(x=iris_data['Petal Length (cm)'], y=iris_data['Sepal Width (cm)'], kind='kde', shade=True)

iris_set_path = os.path.join(file_path, 'iris_setosa.csv')
iris_ver_path = os.path.join(file_path, 'iris_versicolor.csv')
iris_vir_path = os.path.join(file_path, 'iris_virginica.csv')

iris_set_data = pd.read_csv(iris_set_path, index_col='Id')
iris_ver_data = pd.read_csv(iris_ver_path, index_col='Id')
iris_vir_data = pd.read_csv(iris_vir_path, index_col='Id')

# Histograms for each species
sns.distplot(a=iris_set_data['Petal Length (cm)'], label="Iris-setosa", kde=False)
sns.distplot(a=iris_ver_data['Petal Length (cm)'], label="Iris-versicolor", kde=False)
sns.distplot(a=iris_vir_data['Petal Length (cm)'], label="Iris-virginica", kde=False)

# Add title
plt.title("Histogram of Petal Lengths, by Species")

# Force legend to appear
plt.legend()

# KDE plots for each species
sns.kdeplot(data=iris_set_data['Petal Length (cm)'], label="Iris-setosa", shade=True)
sns.kdeplot(data=iris_ver_data['Petal Length (cm)'], label="Iris-versicolor", shade=True)
sns.kdeplot(data=iris_vir_data['Petal Length (cm)'], label="Iris-virginica", shade=True)

# Add title
plt.title("Distribution of Petal Lengths, by Species")
plt.legend()
