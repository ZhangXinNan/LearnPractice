a = [5, 8, 13, 0, 1, 1876, 4]
flag = [0] * (len(a) + 1)

for i,v in enumerate(a):
    if v < len(a):
        flag[v] = 1
print flag

for i,v in enumerate(flag):
    if v==0:
        print i
        break
 
    