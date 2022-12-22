

import time
import numpy as np
import faiss


# Getting some data
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

nlist = 100
k = 4
quantizer = faiss.IndexFlatL2(d)  # the other index
index = faiss.IndexIVFFlat(quantizer, d, nlist)
assert not index.is_trained
t0 = time.time()
index.train(xb)
print("elapse of train:", time.time() - t0)
assert index.is_trained
faiss.write_index(index, "faster.index")

t1 = time.time()
index.add(xb)                  # add may be a bit slower as well
t2 = time.time()
D, I = index.search(xq, k)     # actual search
t3 = time.time()
print(I[-5:])                  # neighbors of the 5 last queries

index.nprobe = 10              # default nprobe is 1, try a few more
D, I = index.search(xq, k)
t4 = time.time()
print(I[-5:])                  # neighbors of the 5 last queries
print("elapse of add:{}, search:{}, {}".format(t2 - t1, t3 - t2, t4 - t3))


