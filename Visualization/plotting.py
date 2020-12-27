import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy.random import randn
from scipy import stats
import seaborn as sns
from matplotlib import interactive

interactive(True)

x = [1, 2, 3]
y = [5, 64, 7]
plt.plot(x, y, label='first line')

dataset_1 = randn(100)
plt.plot(dataset_1, label='test')

dataset_2 = randn(80)
plt.hist(dataset_2, color='indianred')

# Plotting multiple plots in same figure
plt.hist(dataset_1, color='indianred', bins=20, alpha=0.5, density=True)
plt.hist(dataset_2, alpha=0.5, bins=20, density=True)

# Using seaborn for histogram
data_1 = randn(1000)
data_2 = randn(1000)

sns.jointplot(data_1, data_2)
sns.jointplot(data_1, data_2, kind='hex')
