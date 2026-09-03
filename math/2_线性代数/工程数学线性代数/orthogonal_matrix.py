
import math
import numpy as np


P = [[1/2, -1/2, 1/2, -1/2],
     [1/2, -1/2, -1/2, 1/2],
     [1/math.sqrt(2), 1/math.sqrt(2), 0, 0],
     [0, 0, 1/math.sqrt(2), 1/math.sqrt(2)],
     ]
P = np.array(P)
print(P)
print(P.transpose())

result = np.matmul(P, P.transpose())
print(result)

result = np.matmul(P.transpose(), P)
print(result)

