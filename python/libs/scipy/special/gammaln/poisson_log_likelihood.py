import numpy as np
from scipy.special import gammaln

def poisson_log_likelihood(k, lambda_):
    """计算泊松分布的对数似然函数"""
    return k * np.log(lambda_) - lambda_ - gammaln(k + 1)

k = 5
lambda_ = 3.0
log_likelihood = poisson_log_likelihood(k, lambda_)
print(f"Poisson log-likelihood (k={k}, λ={lambda_}) = {log_likelihood}")

