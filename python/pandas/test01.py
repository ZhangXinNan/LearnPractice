#encoding=utf8

import pandas as pd



# Reading a csv into Pandas.
df = pd.read_csv('uk_rain_2014.csv', header=0)

'''
译者注：如果你的数据集中有中文的话，最好在里面加上 encoding = 'gbk' ，以避免乱码问题。后面的导出数据的时候也一样。
'''


'''
准备好要进行探索和分析的数据
'''
# getting first x rows
print df.head(5)
# getting last x rows
print df.tail(5)

# Changing column labels.
df.columns = ['water_year','rain_octsep', 'outflow_octsep',
              'rain_decfeb', 'outflow_decfeb', 'rain_junaug', 'outflow_junaug']
print df.head(5)

# finding out how many rows dataset has.
print len(df)

print  '# Finding out basic statistical information on your dataset.'
pd.options.display.float_format = '{:,.3f}'.format # Limit output to 3 decimal places.
print df.describe()

