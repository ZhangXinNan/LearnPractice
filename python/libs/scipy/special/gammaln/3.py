import numpy as np
from scipy.special import gammaln

a, b = 2.0, 3.0
log_beta = gammaln(a) + gammaln(b) - gammaln(a + b)
print(f"ln(Beta({a}, {b})) = {log_beta}")  # 输出：ln(B(2, 3)) ≈ -2.4849066497880004


