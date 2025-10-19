
'''
numpy.bincount 是 NumPy 库中的一个高效函数，用于统计非负整数数组中每个值的出现次数。它常用于数据分析、统计直方图、概率分布等场景。
以下是对 numpy.bincount 的详细解释，涵盖其定义、参数、返回值、使用场景、代码示例和注意事项。
'''

import numpy as np

x = np.array([0, 1, 1, 2, 0])
counts = np.bincount(x)
print(counts)
# 输出：[2 2 1]
# 解释：
# - 0 出现了 2 次
# - 1 出现了 2 次
# - 2 出现了 1 次

print(np.bincount(np.arange(5)))

print(np.bincount(np.array([0, 1, 1, 3, 2, 1, 7])))

x = np.array([0, 1, 1, 3, 2, 1, 7, 23])
print(np.bincount(x).size == np.amax(x)+1)

