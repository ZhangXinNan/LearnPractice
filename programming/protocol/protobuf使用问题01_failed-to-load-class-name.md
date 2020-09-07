

# 问题
```bash
ERROR: 2020-09-07 11:57:49,512: [root:__init__.py:51] failed to load class name "src.joints_service.JointsService"
Traceback (most recent call last):
  File "/Users/zhangxin/gitlab_md/joints_service/framework/__init__.py", line 48, in loadClass
    m = importlib.import_module(modulename)
  File "/Users/zhangxin/opt/anaconda3/envs/py36_joints/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/Users/zhangxin/gitlab_md/joints_service/src/joints_service.py", line 25, in <module>
    from joints_service_pb2_grpc import JointsServiceServicer, add_JointsServiceServicer_to_server
  File "/Users/zhangxin/gitlab_md/joints_service/interfaces/joints_service_pb2_grpc.py", line 4, in <module>
    import joints_service_pb2 as joints__service__pb2
  File "/Users/zhangxin/gitlab_md/joints_service/interfaces/joints_service_pb2.py", line 24, in <module>
    serialized_pb=_b('\n\x14joints_service.proto\x12\x18\x61llinmd.algorithm.jointsLayer\"\xa7\x01\n\x0bRequestInfo\x12\r\n\x05logid\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x11\n\tsampleids\x18\x03 \x03(\r\x12\x0b\n\x03uip\x18\x04 \x01(\t\x12\x0e\n\x06peerip\x18\x05 \x01(\t\x12\x12\n\naccess_key\x18\x06 \x01(\t\x12\x11\n\tsignature\x18\x07 \x01(\t\x12\r\n\x05\x61ppid\x18\x08 \x01(\r\x12\r\n\x05\x64\x65\x62ug\x18\x64 \x01(\x08J\x04\x08\t\x10\x64\"T\n\x0cResponseInfo\x12/\n\x04\x63ode\x18\x01 \x01(\x0e\x32!.allinmd.algorithm.jointsLayer.RtnCode\x12\r\n\x05\x64\x65\x62ug\x18\x64 \x01(\tJ\x04\x08\x02\x10\x64\"R\n\x0cJointRequest\x12\x33\n\x04info\x18\x01 \x01(\x0b\x32%.allinmd.algorithm.jointsLayer.RequestInfo\x12\r\n\x05image\x18\x02 \x01(\x0c\"0\n\nJointPoint\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\x0c\n\x04name\x18\x03 \x01(\t\"_\n\nJointAngle\x12\x34\n\x06points\x18\x01 \x03(\x0b\x32$.allinmd.algorithm.jointsLayer.JointPoint\x12\r\n\x05\x61ngle\x18\x02 \x01(\x02\x12\x0c\n\x04name\x18\x03 \x01(\t\"\x84\x01\n\rJointResponse\x12\x33\n\x03rtn\x18\x01 \x01(\x0b\x32&.allinmd.algorithm.jointsLayer.ResponseInfo\x12>\n\x10joint_angle_list\x18\x02 \x03(\x0b\x32$.allinmd.algorithm.jointsLayer.JointAngle*m\n\x07RtnCode\x12\x06\n\x02OK\x10\x00\x12\x08\n\x04\x46\x41IL\x10\x01\x12\x19\n\x15\x41UTHENTICATION_FAILED\x10\x64\x12\x16\n\x12INVALID_ACCESS_KEY\x10\x65\x12\x17\n\x13INCORRECT_SIGNATURE\x10\x66\"\x04\x08\x02\x10\x63\x32\xa7\x02\n\rJointsService\x12Y\n\x08shutdown\x12%.allinmd.algorithm.jointsLayer.RequestInfo\x1a&.allinmd.algorithm.jointsLayer.ResponseInfo\x12U\n\x04ping\x12%.allinmd.algorithm.jointsLayer.RequestInfo\x1a&.allinmd.algorithm.jointsLayer.ResponseInfo\x12\x64\n\x11invokeRecognition\x12&.allinmd.algorithm.jointsLayer.JointRequest\x1a\'.allinmd.algorithm.jointsLayer.JointResponseb\x06proto3')
  File "/Users/zhangxin/opt/anaconda3/envs/py36_joints/lib/python3.6/site-packages/google/protobuf/descriptor.py", line 879, in __new__
    return _message.default_pool.AddSerializedFile(serialized_pb)
TypeError: Couldn't parse file content!
ERROR: 2020-09-07 11:57:49,514: [GrpcInterface:grpc_interface.py:55] failed to load grpc service src.joints_service.JointsService
CRITICAL: 2020-09-07 11:57:49,514: [App:__init__.py:165] failed to run GrpcInterface:grpc
INFO: 2020-09-07 11:57:50,518: [ParallelLayer:base_layer.py:68] ParallelLayer:joints prepare to stop
INFO: 2020-09-07 11:57:50,519: [ParallelLayer:base_layer.py:72] ParallelLayer:joints cancelled all tasks
INFO: 2020-09-07 11:57:50,529: [ParallelLayer:base_layer.py:75] ParallelLayer:joints stopped
INFO: 2020-09-07 11:57:50,529: [App:__init__.py:257] all parallel layers stopped
INFO: 2020-09-07 11:57:50,529: [App:__init__.py:262] all interfaces stopped
INFO: 2020-09-07 11:57:50,529: [App:__init__.py:264] app gracefully exited
```


# 解决办法
我当前使用的电脑是Mac，系统是osx。
```
pip uninstall protobuf
pip install --no-binary=protobuf protobuf
```