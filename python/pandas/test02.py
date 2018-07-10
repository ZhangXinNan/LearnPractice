#encoding=utf8

import pandas as pd



# Reading a csv into Pandas.
df = pd.read_csv('uk_rain_2014.csv', header=0)

'''
译者注：如果你的数据集中有中文的话，最好在里面加上 encoding = 'gbk' ，以避免乱码问题。后面的导出数据的时候也一样。
'''

# Changing column labels.
df.columns = ['water_year','rain_octsep', 'outflow_octsep',
              'rain_decfeb', 'outflow_decfeb', 'rain_junaug', 'outflow_junaug']


'''
过滤
'''
print '# Getting a column by label'
print df['rain_octsep']

print '# Getting a column by label using .'
print df.rain_octsep

print '# Creating a series of booleans based on a conditional'
print df.rain_octsep < 1000 # Or df['rain_octsep] < 1000

print '# Using a series of booleans to filter'
print df[df.rain_octsep < 1000]


# Filtering by multiple conditionals
df[(df.rain_octsep < 1000) & (df.outflow_octsep < 4000)] # Can't use the keyword 'and'
'''
注意重要的一点：这里不能用 and 关键字，因为会引发操作顺序的问题。必须用 & 和圆括号。
'''

print '# Filtering by string methods'
print df[df.water_year.str.startswith('199')]
