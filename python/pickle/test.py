import os
import pickle

obj = {}
obj['name'] = 'zhangxin'
obj['age'] = 30
obj['friends'] = {}
obj['friends'] = {'america':['joe','lucy'], 'china':['xiaoming', 'hong']}
print obj
f = open('tmp.bin', 'wb')
pickle.dump(obj, f)

print os.listdir('./')
f = open('tmp.bin', 'rb')
data = pickle.load(f)
print data
