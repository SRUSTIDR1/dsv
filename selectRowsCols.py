import pandas as pd
from pandas import Series, DataFrame

students = [('jack',  34, 'Sydeny',    'Australia'),
            ('Riti',  30, 'Delhi',     'India'),
            ('Vikas', 31, 'Mumbai',    'India'),
            ('Neelu', 32, 'Bangalore', 'India'),
            ('John',  16, 'New York',   'US'),
            ('Mike',  17, 'las vegas',  'US')]

df = DataFrame(students, columns = ['Name', 'Age', 'City', 'Country'], index = ['a', 'b', 'c', 'd', 'e', 'f'])            

# Select a single row of Dataframe
df.loc['a']

# Select multiple rows from Dataframe based on list of names
df.loc[['a', 'c', 'f', 'd']]

# Select multiple rows from Dataframe based on name range
df.loc['b':'e']

# Select rows of Dataframe based on bool array
df.loc[ [True, False, True, False, True, False] ]

# Select rows of Dataframe based on Callable function
df.loc[ lambda x : (x['Age'] > 25) ]

# Select a single column of Dataframe
df.loc[:, 'Age']

# Select multiple columns from Dataframe based on list of names
df.loc[:, ['Age', 'City', 'Name']]

# Select a Cell value from Dataframe
df.loc['c','Name']

# Select subset of Dataframe based on row/column names in list
df.loc[['b', 'd', 'f'],['Name', 'City']]

# Select a single row of Dataframe
df.iloc[2]

# Select multiple rows from Dataframe based on a list of indices
df.iloc[1:4]

