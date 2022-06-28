import numpy as np

def sigmoid(y):
    return 1.0 / (1.0 + np.exp(-y))

def forward(X, w0, w1):
    l1 = sigmoid(np.dot(X, w0))
    l2 = sigmoid(np.dot(l1, w1))
    return l1, l2

X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ]) # 4 * 3
y = np.array([[0,1,1,0]]).T # 4 * 1
syn0 = 2*np.random.random((3,4)) - 1 # 3 * 4
syn1 = 2*np.random.random((4,1)) - 1 # 4 * 1
for j in xrange(60000):
    l1 = sigmoid(np.dot(X, syn0)) # (4) * 4
    l2 = sigmoid(np.dot(l1,syn1)) # (4) * 1
    l2_delta = (y - l2)*(l2*(1-l2)) # (4) * 1
    l1_delta = l2_delta.dot(syn1.T) * (l1 * (1-l1)) # 4 * 4
    syn1 += l1.T.dot(l2_delta) # 4 * 1
    syn0 += X.T.dot(l1_delta) # 3 * 4

l1, l2 = forward(X, syn0, syn1)
print l1
print l2