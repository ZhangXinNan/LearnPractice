import numpy as np
from scipy.special import gammaln

n = 10
log_factorial = gammaln(n + 1)
print(f"ln({n}!) = {log_factorial}")  # 输出：ln(10!) ≈ 12.801827480081469


