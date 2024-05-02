import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('income.csv')
region = list(df['Region'].unique())
colors = ['blue', 'red', 'orange', 'green', 'yellow', 'grey']

colour = {}
for i in range(len(region)):
	colour[region[i]] = colors[i]

fig, ax = plt.subplots()
grouped = df.groupby('Region')

for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='Area', y='Population', s = 'Income', label=key, color=colour[key])    

for i in range(df.shape[0]):
	plt.text(df.iloc[i,3], df.iloc[i,2], df.iloc[i, 0])
plt.show()