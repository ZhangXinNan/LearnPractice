
这个参数乘上你的train prototxt中的batch size是你实际使用的batch size。 相当于读取batchsize*itersize个图像才做一下gradient decent。 这个参数可以规避由于gpu不足而导致的batchsize的限制 因为你可以用多个iteration做到很大的batch 即使单次batch有限



参考资料：
[Caffe中的batch_size和iter_size](https://zhuanlan.zhihu.com/p/43700021)
[caffe SolverParameter中的iter_size参数什么作用？](https://www.zhihu.com/question/37270367)