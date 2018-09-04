
问题：
```
2018-08-29 13:52:55.579348: E tensorflow/core/common_runtime/direct_session.cc:158] Internal: cudaGetDevice() failed. Status: CUDA driver version is insufficient for CUDA runtime version
Traceback (most recent call last):
  File "elg_demo.py", line 52, in <module>
    with tf.Session(config=session_config) as session:
  File "/home/zhangxin/anaconda3/envs/py36_gazeml/lib/python3.6/site-packages/tensorflow/python/client/session.py", line 1494, in __init__
    super(Session, self).__init__(target, graph, config=config)
  File "/home/zhangxin/anaconda3/envs/py36_gazeml/lib/python3.6/site-packages/tensorflow/python/client/session.py", line 626, in __init__
    self._session = tf_session.TF_NewSession(self._graph._c_graph, opts)
tensorflow.python.framework.errors_impl.InternalError: Failed to create session.
```

解决方法：
这个虚拟环境有问题，从另一个测试正常的复制一份
```
conda create -n py3.6_tf_clone_gazeml --clone py3.6_tf
```



