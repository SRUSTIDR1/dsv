import pandas as pd
from pandas import Series, DataFrame

df = DataFrame([[1,2],[3,4]], columns = ['one', 'two'])

# Add row to existing dataframe
df.loc[df.shape[0]] = [5,6]
df.loc[df.shape[0]] = df.sum()

# Delete row/s from dataframe
df = df.drop(index=3)		# drop row with index 3
df = df.drop(df.index[3:5])	# drop row with index 3 and 4 not 5

# delete row based on value of cell
df = df.drop(index = df[df['one'] == 25].index)

# Add column
df['sum'] = df.sum(axis = 1)	# add column with name 'sum'. axis = 1 sum values of each row. Row sum

# Delete column 
df = df.drop('sum', axis = 1)
df.drop('sum', axis = 1, inplace=True)
df.drop(['sum','avg'], axis = 1, inplace=True)
del df['sum']