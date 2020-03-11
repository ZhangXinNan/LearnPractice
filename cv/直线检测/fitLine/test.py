

import numpy as np
import cv2

a = [[0, 0], [0, 1]]
b = [[0, 0], [1, 0]]
c = [[0, 0], [0, -1]]
d = [[0, 0], [-1, 0]]
e = [[0, 0], [1, 1]]

la = cv2.fitLine(np.array(a), cv2.DIST_L2, 0, 0.01, 0.01)
lb = cv2.fitLine(np.array(b), cv2.DIST_L2, 0, 0.01, 0.01)
lc = cv2.fitLine(np.array(c), cv2.DIST_L2, 0, 0.01, 0.01)
ld = cv2.fitLine(np.array(d), cv2.DIST_L2, 0, 0.01, 0.01)
le = cv2.fitLine(np.array(e), cv2.DIST_L2, 0, 0.01, 0.01)
print(la)
print(lb)
print(lc)
print(ld)
print(le)

