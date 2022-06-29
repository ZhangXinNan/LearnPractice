
# 0 准备工作
1. 安装nvidia显卡驱动
2. 安装cuda
3. 安装cudnn，实际就是下载后拷贝到cuda目录下。
4. 安装conda，创建虚拟环境
5. 下载[TensorRT](https://developer.nvidia.com/nvidia-tensorrt-download)。

# 1 在python环境中安装tensorrt
1. Install the following dependencies, if not already present:
* CUDA 10.2, 11.0 update 1, 11.1 update 1, 11.2 update 2, 11.3 update 1, or 11.4 update 2
* cuDNN 8.2.1
* Python 3 (Optional)

2. Download the TensorRT tar file that matches the CPU architecture and CUDA version you are using.

3. Choose where you want to install TensorRT. This tar file will install everything into a subdirectory called TensorRT-8.x.x.x.

4. Unpack the tar file.
version="8.x.x.x"
arch=$(uname -m)
cuda="cuda-x.x"
cudnn="cudnn8.x"
tar xzvf TensorRT-${version}.Linux.${arch}-gnu.${cuda}.${cudnn}.tar.gz
Where:
8.x.x.x is your TensorRT version
cuda-x.x is CUDA version 10.2 or 11.4
cudnn8.x is cuDNN version 8.2
This directory will have sub-directories like lib, include, data, etc…
ls TensorRT-${version}
bin  data  doc  graphsurgeon  include  lib  onnx_graphsurgeon  python  samples  targets  TensorRT-Release-Notes.pdf  uff

5. Add the absolute path to the TensorRTlib directory to the environment variable LD_LIBRARY_PATH:
```bash
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:<TensorRT-${version}/lib>
```

6. Install the Python TensorRT wheel file.
```bash
cd TensorRT-${version}/python

python3 -m pip install tensorrt-*-cp3x-none-linux_x86_64.whl
```

7. Install the Python UFF wheel file. This is only required if you plan to use TensorRT with TensorFlow.
```bash
cd TensorRT-${version}/uff

python3 -m pip install uff-0.6.9-py2.py3-none-any.whl
```
Check the installation with:
```bash
which convert-to-uff
```

8. Install the Python graphsurgeon wheel file.
```bash
cd TensorRT-${version}/graphsurgeon

python3 -m pip install graphsurgeon-0.4.5-py2.py3-none-any.whl
```

9. Install the Python onnx-graphsurgeon wheel file.
```bash
cd TensorRT-${version}/onnx_graphsurgeon
	
python3 -m pip install onnx_graphsurgeon-0.3.12-py2.py3-none-any.whl
```

10.  Verify the installation:
Ensure that the installed files are located in the correct directories. For example, run the ```tree -d``` command to check whether all supported installed files are in place in the lib, include, data, etc… directories.
Build and run one of the shipped samples, for example, sampleMNIST in the installed directory. You should be able to compile and execute the sample without additional settings. For more information, see the “Hello World” For TensorRT (sampleMNIST).
The Python samples are in the samples/python directory.

# 2 pycuda 安装
```bash
pip install pycuda
```


# 参考资料
* [NVIDIA TENSORRT installation guide](https://docs.nvidia.com/deeplearning/tensorrt/install-guide/index.html#installing-pip)
* [NVIDIA TENSORRT installation guide](https://docs.nvidia.com/deeplearning/tensorrt/install-guide/index.html#installing-tar)

