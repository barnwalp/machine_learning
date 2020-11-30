import gspread
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive

interactive(True)

x = [1, 2, 3]
y = [5, 64, 7]

plt.plot(x, y, label='first line')
plt.show()
gc = gspread.service_account(filename='credential.json')
sh = gc.open_by_key('1c8GkIHjMkcmapbvEwDkBSQACzChlLROnfPXPlJJ8Txs')
data = sh.worksheet('data_transfer').get_all_values()
df = pd.DataFrame(data)
print('hello world')
