[smallcorgi/Faster-RCNN_TF](https://github.com/smallcorgi/Faster-RCNN_TF)

# 安装问题
## 142
### 问题1
```
2017-09-27 16:21:16.725103: W tensorflow/core/framework/op_kernel.cc:1182] Invalid argument: Cannot parse tensor from proto: dtype: DT_FLOAT
```



## 143
### 问题1
``` 
2017-09-27 14:55:08.649781: E tensorflow/stream_executor/cuda/cuda_driver.cc:893] failed to allocate 2.2K (2304 bytes) from device: CUDA_ERROR_INVALID_VALUE
```
解决方法：
```
os.environ['CUDA_VISIBLE_DEVICES'] = str(3)
```