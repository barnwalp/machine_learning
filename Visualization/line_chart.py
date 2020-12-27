import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib import interactive


interactive(True)
# to show the sns and plt plots
plt.show()

# dataset path: it assumes that it is in git_repo directory
file_path = os.path.join(os.getcwd(), 'datasets', 'kaggle_dataset')
spotify_path = os.path.join(file_path, 'spotify.csv')
spotify_data = pd.read_csv(spotify_path, index_col="Date", parse_dates=True)

# Set the width and height of the figure
plt.figure(figsize=(14,6))

# Add title
plt.title("Daily Global Streams of Popular Songs in 2017-2018")

# Line chart showing daily global streams of each song
sns.lineplot(data=spotify_data)

# Line chart showing daily global streams of 'Shape of You'
sns.lineplot(data=spotify_data['Shape of You'], label="Shape of You")

# Line chart showing daily global streams of 'Despacito'
sns.lineplot(data=spotify_data['Despacito'], label="Despacito")

# Add label for horizontal axis
plt.xlabel("Date")

# Add label for vertical axis
plt.ylabel("Popular Songs")
