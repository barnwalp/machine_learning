import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib import interactive


interactive(True)
pd.set_option('max_columns', None)

data_path = os.path.join(os.getcwd(), 'datasets', 'kaggle_dataset')
file_path = os.path.join(data_path, 'insurance.csv')
insurance_data = pd.read_csv(file_path)

plt.figure(figsize=(10, 5))
plt.title('Relation between charges vs bmi')
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])

# to find the regression line along with scatter plot
sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])

# To plot the data using third variable
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])

# to plot 2 regression lines using hue variable
sns.lmplot(x='bmi', y='charges', hue='smoker', data=insurance_data)

# To plot categorical scatter plot
sns.swarmplot(x=insurance_data['smoker'], y=insurance_data['charges'])
