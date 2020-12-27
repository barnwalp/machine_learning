import numpy as np
import pandas as pd


# manually creating dataframe
df = pd.DataFrame({
    'Population': [35.467, 63.951, 80.94 , 60.665, 127.061, 64.511, 318.523],
    'GDP': [
        1785387,
        2833687,
        3874437,
        2167744,
        4602367,
        2950039,
        17348075
    ],
    'Surface Area': [
        9984670,
        640679,
        357114,
        301336,
        377930,
        242495,
        9525067
    ],
    'HDI': [
        0.913,
        0.888,
        0.916,
        0.873,
        0.891,
        0.907,
        0.915
    ],
    'Continent': [
        'America',
        'Europe',
        'Europe',
        'Europe',
        'Asia',
        'Europe',
        'America'
    ]
}, columns=['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])

# Creating index for the dataframe
df.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
]

# Selecting a row based on the index
df.loc['Canada']
# Selecting a row based on sequential index
df.iloc[0]

# Selecting the columns
df['Population']
# Selecting multiple columns
df[['Population', 'GDP']]

# selecting multiple rows; from 1 upto 2nd row
df.iloc[1:3]
# selecting multiple rows; from 1 upto 3rd row
df.loc['France': 'Italy']
# Second arguments can be added for columns
df.loc['France': 'Italy', 'Population']
df.loc['France': 'Italy', ['Population', 'GDP']]
df.iloc[1:3, [0, 3]]

# Conditional Selection
df.loc[df['Population'] > 70]
df.loc[df['Population'] > 70, ['Population', 'GDP']]

# Dropping rows
df.drop(['Canada', 'Japan'])
# Given that df.index returns all indices value, any of them
# can be selected with [] operator
df.drop(df.index[1])

# Dropping columns
df.drop(['Population', 'HDI'], axis=1)
# Dropping columns
df.drop(['Italy', 'Canada'], axis=0)

# Operation
df[['Population', 'GDP']] / 100

# Radical index changes
df.reset_index()
df.set_index('Population')

# Creating columns from other columns
df['GDP Per Capita'] = df['GDP'] / df['Population']
