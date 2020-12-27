import pandas as pd
import numpy as np


# Unlike python list, pandas series has a datatype
g7_pop = pd.Series([35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523])

# datatype of pandas series
print(g7_pop.dtype)

# In contrast to the list, index can be explicitly defined
g7_pop.index = [
    'Canada',
    'Franc',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
]

test = pd.Series({
    'Canada': 35,
    'France': 63,
    'Japan': 88,
    'Italy': 68
    }, name='G7 population in million')

# indexing
print(g7_pop['Canada'])

# Numeric position can be used using iloc attributes
print(g7_pop.iloc[0])
print(g7_pop.iloc[-1])

# getting multiple columns of the series
print(g7_pop[['Canada', 'Japan']])

# getting multiple columns using iloc
print(g7_pop.iloc[[0, 1]])

# slicing in pandas
g7_pop['Canada': 'Italy']

# Conditional Selection (boolean arrays)
print(g7_pop > 70)
print(g7_pop[g7_pop > 70])
print(g7_pop[g7_pop > g7_pop.mean()])
print(g7_pop[(g7_pop > g7_pop.mean() - g7_pop.std() /2) | (g7_pop > g7_pop.mean() + g7_pop.std() /2)])

#####################################################
# Create an empty pandas series
print(pd.Series(dtype=float))

# Convert a list to a pandas series
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = pd.Series(li)
print(x)

# Convert the given integer pandas series to float
pd.Series(x, dtype=float)

# sort the given pandas series
x.sort_values(inplace=True, ascending=False)
print(x)
