
from pandas import Series, DataFrame
import pandas as pd
# print(pd.__version__)

'''
# Series
Series 是一种类似于存储一维数组的对象，它由一组数据和与之相关的标签组成。
'''
print('如果没有为它创建索引的情况下，它会像数组一样自动创建0到N-1的索引。')
obj = Series([4, 7, -5, 3])
print('obj:', obj)
print('obj.index:', obj.index)
print('obj.values:', obj.values)
'''
输出：
0    4
1    7
2   -5
3    3
dtype: int64
RangeIndex(start=0, stop=4, step=1)
[ 4  7 -5  3]
'''


print('# 创建一个带索引的Series')
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print('obj2[a]:', obj2['a'])
obj2['d'] = 6
print('obj2[d]:', obj2['d'])
print(obj2[['c', 'a', 'd']])
print(obj2[obj2 > 0])
'''
obj2[a]: -5
obj2[d]: 6
c    3
a   -5
d    6
dtype: int64
d    6
b    7
c    3
dtype: int64
'''


