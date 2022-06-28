
import re


print('匹配')
r = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(r)

r = re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
print(r)

print('切分字符串')
s = re.split(r'\s+', 'a b   c')
print(s)

s = re.split(r'[\s\,]+', 'a,b, c  d')
print(s)


print("分组")
# m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# print(m, m.group(0), m.group(1), m.group(2))
print(re.match(r'^(\d{3})-(\d{3,8})$', '010-12345').groups())

print('贪婪匹配')
m = re.match(r'^(\d+)(0*)$', '102300').groups()
print(m)

print('非贪婪匹配')
m = re.match(r'^(\d+?)(0*)$', '102300').groups()
print(m)

print('编译')
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())


print("检索和替换")
phone = "2004-959-559 # 这是一个国外电话号码"
 
# 删除字符串中的 Python注释 
num = re.sub(r'#.*$', "", phone)
print("电话号码是: ", num)
 
# 删除非数字(-)的字符串 
num = re.sub(r'\D', "", phone)
print("电话号码是 : ", num)