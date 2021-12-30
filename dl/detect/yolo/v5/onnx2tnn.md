

下载TNN代码
```bash
git clone git@github.com:Tencent/TNN.git
```

安装docker
```bash

```

获取镜像

```bash
docker pull ccr.ccs.tencentyun.com/qcloud/tnn-convert

docker tag ccr.ccs.tencentyun.com/qcloud/tnn-convert tnn-convert:latest
docker rmi ccr.ccs.tencentyun.com/qcloud/tnn-convert
```

或者，直接创建镜像
```bash
cd ~/github/TNN
docker build -t tnn-convert:latest .
```


转换模型
```bash
# tf2tnn
# docker run  -it tnn-convert:latest  python3 ./converter.py tf2tnn -h
docker run --volume=$(pwd):/workspace -it tnn-convert:latest  python3 ./converter.py tf2tnn -tp=/workspace/test.pb -in=input0,input2 -on=output0 -v=v2.0 -optimize
# onnx2tnn
# docker run  -it tnn-convert:latest  python3 ./converter.py onnx2tnn -h
docker run --volume=$(pwd):/workspace -it tnn-convert:latest python3 ./converter.py onnx2tnn /workspace/mobilenetv3-small-c7eb32fe.onnx -optimize -v=v3.0

docker run --volume=$(pwd):/workspace -it tnn-convert:latest python3 ./converter.py onnx2tnn /workspace/yolov5s.onnx -optimize -v=v3.0
```

