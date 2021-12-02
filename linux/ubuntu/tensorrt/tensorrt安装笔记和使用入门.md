

# 0 准备工作
查看操作系统版本
```bash
lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.5 LTS
Release:        18.04
Codename:       bionic
```

查看显卡驱动
```
(base) ➜  ~ nvidia-smi  
Thu Dec  2 04:45:11 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 470.57.02    Driver Version: 470.57.02    CUDA Version: 11.4     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Quadro RTX 6000     Off  | 00000000:17:00.0 Off |                  Off |
| 33%   31C    P8    10W / 260W |      1MiB / 24220MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   1  Quadro RTX 6000     Off  | 00000000:73:00.0 Off |                  Off |
| 33%   33C    P8    16W / 260W |      1MiB / 24211MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```


查看cuda安装情况，cuda-11.1

下载tensorrt，TensorRT-7.2.3.4.Ubuntu-18.04.x86_64-gnu.cuda-11.1.cudnn8.1.tar.gz。

# 1 简单的TensorRT例子
## 1.1 转换Pytorch图像分割模型为onnx模型。
```bash
sudo apt-get install libprotobuf-dev protobuf-compiler # protobuf is a prerequisite library
git clone --recursive https://github.com/onnx/onnx.git # Pull the ONNX repository from GitHub 
cd onnx
mkdir build && cd build
cmake .. # Compile and install ONNX
make # Use the ‘-j’ option for parallel jobs, for example, ‘make -j $(nproc)’ 
make install
cd ../..
git clone https://github.com/parallel-forall/code-samples.git
cd code-samples/posts/TensorRT-introduction
make clean && make # Compile the TensorRT C++ code
cd ..
wget https://developer.download.nvidia.com/devblogs/speeding-up-unet.7z // Get the ONNX model and test the data
tar xvf speeding-up-unet.7z # Unpack the model data into the unet folder
cd unet
python create_network.py #Inside the unet folder, it creates the unet.onnx file
```


## 1.2 引入onnx模型到TensorRT。
## 1.3 应用优化生成引擎。
## 1.4 在GPU上执行推理。




