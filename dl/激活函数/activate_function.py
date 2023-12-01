
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

x = np.arange(-10, 10)
fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(x, sigmoid(x), 'r')
plt.show()

x = np.linspace(10, 10, 100)
y = np.tanh(x)
plt.plot(x, y)
plt.show()


