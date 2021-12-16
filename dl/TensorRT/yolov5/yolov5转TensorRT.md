

# 下载yolov5代码、模型
[yolov5](https://github.com/ultralytics/yolov5)
[tensorrtx](https://github.com/wang-xinyu/tensorrtx)


# 环境准备
1. 安装cuda/cudnn/tensorrt
2. 安装pycuda
3. 生成wts文件
```bash
python gen_wts.py -w yolov5x.pt -o yolovx.wts
```

4. 编译
```bash
cd yolov5
mkdir build && cd build
cmake ..
make
```

5. 生成engine文件
```bash
./yolov5 -s yolov5x.wts yolov5x.engine x
```












