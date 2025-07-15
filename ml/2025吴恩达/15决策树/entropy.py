
import math


def H(p1):
    p0 = 1 - p1
    return -p1 * math.log2(p1) - p0 * math.log2(p0)


p1 = 4/5
h = H(p1)
print(p1, h)

p1 = 1/5
h = H(p1)
print(p1, h)


p1 = 4/7
h = H(p1)
print(p1, h)

p1 = 1/3
h = H(p1)
print(p1, h)



p1 = 3/4
h = H(p1)
print(p1, h)

p1 = 2/6
h = H(p1)
print(p1, h)