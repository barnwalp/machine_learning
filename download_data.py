import os
import tarfile
import urllib.request
import pandas as pd

url_link = 'https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.tgz'
# It will create a recurcice folder datasets/housing
# os.chdir('c:\\Users\\panka')
housing_path = os.path.join('datasets', 'housing')

def fetch_housing_data(url_link, housing_path):
    os.makedirs(housing_path, exist_ok=True)
    target_path = os.path.join(housing_path, 'housing.tgz')
    # This will auto download the file attached to url and put it in
    # target_path, downloaded file's name will be dictated by target_path
    urllib.request.urlretrieve(url_link, target_path)
    housing_tgz = tarfile.open(target_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

fetch_housing_data(url_link, housing_path)

def load_housing_data(housing_path):
    csv_path = os.path.join(housing_path, 'housing.csv')
    return pd.read_csv(csv_path)

file_path = os.path.join(os.getcwd(), 'github_repo', housing_path)
housing = load_housing_data(file_path)
housing.head()
