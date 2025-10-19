import numpy as np
from scipy.special import gammaln

z = 3 + 4j
print(z)
result = gammaln(z)
print(f"ln|Gamma({z})| = {result}")  # 输出：复数结果

