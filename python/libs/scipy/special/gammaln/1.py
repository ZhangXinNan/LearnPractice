import numpy as np
from scipy.special import gammaln

# 标量输入
z = 5
result = gammaln(z)
print(f"ln|Gamma({z})| = {result}")  # 输出：ln|Gamma(5)| = ln(4!) = ln(24) ≈ 3.1780538303479458

# 数组输入
z_array = np.array([1, 2, 3, 4, 5])
result_array = gammaln(z_array)
print(f"ln|Gamma(z_array)| = {result_array}")
# 输出：[0.         0.         0.69314718 1.79175947 3.17805383]



