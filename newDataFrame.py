import pandas as pd
from pandas import Series, DataFrame

# Create DF using Dictionary

def createDFByDictionary():
	inputdata = {'RegNo':[2001, 2002, 2003], 'Name':['ABC', 'DEF', 'GHI'], 'GPA':[8.3, 9.1, 7.98]}
	df = pd.DataFrame(data = inputdata)
	#print (df)
	# Column name and index settings
	df = DataFrame(data = inputdata, columns = ['Name', 'GPA', 'RegNo'], index = ['A', 'B', 'C'])
	print (df)

	return df

def createDFByTuples():
	students = [('jack',  34, 'Sydeny',    'Australia'),
            ('Riti',  30, 'Delhi',     'India'),
            ('Vikas', 31, 'Mumbai',    'India'),
            ('Neelu', 32, 'Bangalore', 'India'),
            ('John',  16, 'New York',   'US'),
            ('Mike',  17, 'las vegas',  'US')]

	df = DataFrame(students, columns = ['Name', 'Age', 'City', 'Country'], index = ['a', 'b', 'c', 'd', 'e', 'f'])
	print (df)

	return df


def createDFByList():
	names = ['SUB1', 'SUB2', 'SUB3']
	mark_sub1 = [87, 90, 65]
	mark_sub2 = [67, 71, 81]
	mark_sub3 = [78, 73, 75]

	marks = list(zip(mark_sub1, mark_sub2, mark_sub3))
	df = DataFrame(marks, columns = names)
	print (df)

	return df

def createDFFromFile(fname):
	df = pd.read_excel(fname)
	print (df)

	return df


#print ('By Dictionary')
#createDFByDictionary()

#print('By Tuple')
#createDFByTuples()

#print ('By List')
#createDFByList()

print ('From File')
excel_file_path = 'D:/Dataset/FIFA2022 Final.xlsx'
createDFFromFile(excel_file_path)
