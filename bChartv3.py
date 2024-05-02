import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('products.xlsx')


x = [1,2,3,4]
y_A = list(df.iloc[0,1:])
y_B = list(df.iloc[1,1:])
y_C = list(df.iloc[2,1:])
width = 0.6

plt.bar(x,y_A, color = 'red', label ='Product A', width = width)
plt.bar(x, y_B, bottom = y_A, color = 'blue', label = 'Product B', width = width)
plt.bar(x, y_C, bottom = [y_A[i] + y_B[i] for i in range(len(y_A))], color = 'green', label = 'Product C', width = width)

plt.xticks(x, [2018, 2019, 2020, 2021])
plt.legend()

plt.xlabel('Year')
plt.ylabel('Profit in Crores')
plt.title('Profit of Products Yearwise')
plt.show()
