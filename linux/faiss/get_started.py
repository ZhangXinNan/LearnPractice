
import time
import numpy as np
import faiss

# Getting some data
'''
d = 64                           # dimension
nb = 100000                      # database size
nq = 10000                       # nb of queries
'''
d = 256
nb = 100 * 10000
nq = 100
np.random.seed(1234)             # make reproducible

# 训练数据
xb = np.random.random((nb, d)).astype('float32')
xb[:, 0] += np.arange(nb) / 1000.
print("xb : ", xb.shape, xb.dtype)

# 查询数据
xq = np.random.random((nq, d)).astype('float32')
xq[:, 0] += np.arange(nq) / 1000.
print("xq : ", xq.shape, xq.dtype)


# Building an index and adding the vectors to it
index = faiss.IndexFlatL2(d)   # build the index
print(index.is_trained)
t0 = time.time()
index.add(xb)                  # add vectors to the index
print("elapse of add:", time.time() - t0)
print(index.ntotal)
faiss.write_index(index, "index.index")

# Searching
k = 4                          # we want to see 4 nearest neighbors
D, I = index.search(xb[:5], k) # sanity check
print(I)
print(D)
t0 = time.time()
D, I = index.search(xq, k)     # actual search
print("elapse of search: ", time.time() - t0)
print(I[:5])                   # neighbors of the 5 first queries
print(I[-5:])                  # neighbors of the 5 last queries



