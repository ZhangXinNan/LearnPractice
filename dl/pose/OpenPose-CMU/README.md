

[CMU-Perceptual-Computing-Lab/openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)

# 克隆代码
```bash
git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose
cd openpose/
git submodule update --init --recursive --remote
```


# 编译
```bash
mkdir build
cd build
cmake ..
make -j

cmake .. -DBUILD_PYTHON=ON \
    -DPYTHON_EXECUTABLE=/home/zhangxin/miniconda3/envs/py36_pose/bin/python3.6 \
    -DPYTHON_LIBRARY=/home/zhangxin/miniconda3/envs/py36_pose/lib/libpython3.6m.so

```


# quick start
```bash
# Ubuntu
./build/examples/openpose/openpose.bin --video examples/media/video.avi

# Windows - Portable Demo
bin\OpenPoseDemo.exe --video examples\media\video.avi
```

# PYTHON
```bash
python3 01_body_from_image.py
python3 02_whole_body_from_image.py
```






