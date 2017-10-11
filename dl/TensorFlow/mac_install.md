# virtualenv
## 问题1 TypeError: __init__() got an unexpected keyword argument 'syntax'
```
(tensorflow) ➜  ~ python
Python 2.7.13 (default, Apr  4 2017, 08:46:44) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/site-packages/tensorflow/__init__.py", line 24, in <module>
    from tensorflow.python import *
  File "/usr/local/lib/python2.7/site-packages/tensorflow/python/__init__.py", line 54, in <module>
    from tensorflow.core.framework.graph_pb2 import *
  File "/usr/local/lib/python2.7/site-packages/tensorflow/core/framework/graph_pb2.py", line 16, in <module>
    from tensorflow.core.framework import node_def_pb2 as tensorflow_dot_core_dot_framework_dot_node__def__pb2
  File "/usr/local/lib/python2.7/site-packages/tensorflow/core/framework/node_def_pb2.py", line 16, in <module>
    from tensorflow.core.framework import attr_value_pb2 as tensorflow_dot_core_dot_framework_dot_attr__value__pb2
  File "/usr/local/lib/python2.7/site-packages/tensorflow/core/framework/attr_value_pb2.py", line 16, in <module>
    from tensorflow.core.framework import tensor_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__pb2
  File "/usr/local/lib/python2.7/site-packages/tensorflow/core/framework/tensor_pb2.py", line 16, in <module>
    from tensorflow.core.framework import resource_handle_pb2 as tensorflow_dot_core_dot_framework_dot_resource__handle__pb2
  File "/usr/local/lib/python2.7/site-packages/tensorflow/core/framework/resource_handle_pb2.py", line 22, in <module>
    serialized_pb=_b('\n/tensorflow/core/framework/resource_handle.proto\x12\ntensorflow\"m\n\x0eResourceHandle\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\t\x12\x11\n\tcontainer\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x11\n\thash_code\x18\x04 \x01(\x04\x12\x17\n\x0fmaybe_type_name\x18\x05 \x01(\tB4\n\x18org.tensorflow.frameworkB\x13ResourceHandleProtoP\x01\xf8\x01\x01\x62\x06proto3')
TypeError: __init__() got an unexpected keyword argument 'syntax'
```

 解决方法

 ```
 pip uninstall protobuf
 brew uninstall protobuf
 source ~/tensorflow/bin/activate
 pip install tensorflow
 ```

 ## 问题2 无法卸载protobuf
 ```
 ➜  ~ pip uninstall protobuf
Cannot uninstall requirement protobuf, not installed
 ```

解决方法
```
brew uninstall protobuf
```