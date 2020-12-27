import numpy as np
from numpy.random import randn
import pandas as pd
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import interactive


interactive(True)
# to show the sns and plt plots
plt.show()

dataset = randn(25)
plt.hist(dataset, alpha=0.3)
sns.rugplot(dataset)
# setting lower and upper ylimit as 0 & 1
# plt.ylim(0, 1)

x_min = dataset.min()-2
x_max = dataset.max()+2

# create the axis with 100 equally space points
x_axis = np.linspace(x_min, x_max, 100)

bandwidth = ((4*dataset.std()**5)/(3*len(dataset))) ** 0.2
kernel_list = []

for data_point in dataset:
    # create a kernel for each points and append to the kernel list
    kernel = stats.norm(data_point, bandwidth).pdf(x_axis)
    kernel_list.append(kernel)
    # scale for plotting
    kernel = kernel /kernel.max()
    kernel = kernel * 0.45
    plt.plot(x_axis, kernel, color='gray', alpha=0.5)
    plt.ylim(0, 1)

sum_of_kde = np.sum(kernel_list, axis=0)
fig = plt.plot(x_axis, sum_of_kde, color='indianred')
sns.rugplot(dataset)
# plt.yticks([])
plt.suptitle("Sum of the basis function")

sns.kdeplot(dataset, legend=True)
plt.legend('test')
sns.rugplot(dataset, color='black')
for bw in np.arange(0.5, 2, 0.25):
    sns.kdeplot(dataset, bw=bw, lw=1.8)

plt.title('kdeplot for different bandwidth')

data = randn(100)
# Using distplot to plot hist and kdeplot
sns.distplot(data, bins=25)

# Using distplot to plot hist and rugplot
sns.distplot(data, bins=25, rug=True, hist=False)

# Note: label does not work here
sns.distplot(data, bins=25,
        kde_kws={'color': 'indianred', 'label': 'KDE Plot'},
        hist_kws={'color': 'blue', 'label': 'hist'})

