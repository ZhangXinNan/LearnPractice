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

# 第4列小于第6列的
# df = df[df.rain_decfeb < df.rain_junaug]
# print df


print df[df.rain_decfeb < df.rain_junaug].index
df.drop(df.rain_decfeb < df.rain_junaug)
# print df