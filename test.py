import pandas as pd
import matplotlib.pyplot as plt

mydata = pd.read_csv('result\\skew.csv', index_col=0)
mydata['Date'] = pd.to_datetime(mydata['Date'])
plt.figure(figsize=(10,3))
plt.plot(mydata['Date'], mydata['skew'])
plt.show()

a = 1