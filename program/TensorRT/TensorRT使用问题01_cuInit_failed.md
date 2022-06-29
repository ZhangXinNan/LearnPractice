

# 问题

```bash
(py37_auto_service) ➜  src git:(zxdev_trt) ✗ python classifier_trt.py
Traceback (most recent call last):
  File "classifier_trt.py", line 13, in <module>
    import common
  File "/usr/local/TensorRT-7.2.3.4/samples/python/common.py", line 55, in <module>
    import pycuda.autoinit
  File "/home/zhangxin/miniconda3/envs/py37_auto_service/lib/python3.7/site-packages/pycuda/autoinit.py", line 5, in <module>
    cuda.init()
pycuda._driver.Error: cuInit failed: unknown error
```

# 解决办法


如果是本来没问题，重启电脑就好了。


