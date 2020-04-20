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
对数据集应用函数
'''
# Applying a function to a column
def base_year(year):
    base_year = year[:4]
    base_year= pd.to_datetime(base_year).year
    return base_year

df['year'] = df.water_year.apply(base_year)
print df.head(5)


'''
操作数据集的结构
'''
#Manipulating structure (groupby, unstack, pivot)
# Grouby
df.groupby(df.year // 10 *10).max()


