import os
import tarfile
import urllib.request

root_url = 'https://raw.githubusercontent.com/ageron/handson-ml2/master/'
# This will create a path datasets/housing which in turn will create
# recursive folders
os.chdir('c:\\Users\\panka')
print(os.getcwd())
housing_path = os.path.join('Documents', 'datasets', 'housing')
housing_url = root_url + 'datasets/housing/housing.tgz'

def fetch_housing_data(housing_url=housing_url, housing_path=housing_path):
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, 'housing.tgz')
    # This will auto download the file attached to url and put it in
    # tgz_path, downloaded file's name will be dictated by tgz_path
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    print(housing_tgz)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

fetch_housing_data(housing_url=housing_url, housing_path=housing_path)
