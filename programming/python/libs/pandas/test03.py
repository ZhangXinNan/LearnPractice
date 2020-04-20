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
索引
'''

# Getting a row via a numerical index
print df.iloc[30]


# Setting a new index from an existing column
df = df.set_index(['water_year'])
print df.head(5)


# Getting a row via a label-based index
print df.loc['2000/01']


# Getting a row via a label-based or numerical index
print df.ix['1999/00'] # Label based with numerical index fallback *Not recommended

# 可以对 dataframe 调用 sort_index 方法进行排序。
df.sort_index(ascending=False).head(5) #inplace=True to apple the sorting in place
print df


# Returning an index to data
df = df.reset_index('water_year')
df.head(5)