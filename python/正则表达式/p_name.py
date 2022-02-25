
#正则 分组
'''
1. re.match,re.search,re.finditer 的返回值均为m=<re.Match object; span=(0, 1), match='她'>类型，
    若想获得匹配值的位置：m.span()；
    若想获得匹配值的内容，m.group()；
    特殊：re.finditer返回的为迭代器需要循环输出
2. re.sub返回替换后的内容
3. re.findall 返回匹配值的列表
4. ?P<value1>为组名，可根据组名定位匹配值的位置， 注意：是在.group()中的标记
'''
import re
def double(x):# 将匹配的数字乘以 2
    value = int(x.group('value'))
    return str(value * 2)
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))#A46G8HFD1134
print("="*30)
 
#group(0)
a = "123abc456"
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0))   #123abc456,返回整体
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1))   #123
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2))  #abc
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3))   #456
print("="*30)
 
#贪婪匹配与非贪婪匹配
ret_greed= re.search(r'(?P<value1>\d+)(.+?)([a-z]*)(?P<value2>\d+)','12*%@abc45')
print('###贪婪：',ret_greed)
print('分组group(0)：',ret_greed.group(0))#12*%@abc45
print('分组group(value1)：',ret_greed.group('value1'))#12
print('分组group(1)：',ret_greed.group(1))#12
print('分组group(2)：',ret_greed.group(2))#*%@
print('分组group(3)：',ret_greed.group(3))#abc
print('分组group(4)：',ret_greed.group(4))#45
print('分组groupdict：',ret_greed.groupdict())#{'value1': '12', 'value2': '45'}
 
 
ret_no_greed= re.findall(r'a(\d+?)','a23b')# ['2']
print('###非贪婪：',ret_no_greed)


