
# 1 部署
## 1.1 使用开发镜像
* [使用Docker安装Paddle Serving](https://github.com/PaddlePaddle/Serving/blob/v0.9.0/doc/Install_CN.md)
* [Install Paddle Serving with Docker](https://github.com/PaddlePaddle/Serving/blob/v0.9.0/doc/Install_EN.md)

```bash
# 启动 GPU Docker
docker pull registry.baidubce.com/paddlepaddle/serving:0.9.0-cuda11.2-cudnn8-devel
nvidia-docker run -p 9299:9299 --name gpu_paddle_serving -dit registry.baidubce.com/paddlepaddle/serving:0.9.0-cuda11.2-cudnn8-devel bash
nvidia-docker exec -it gpu_paddle_serving bash
```

## 1.2 安装wheel包
[2.安装 Wheel 包](https://github.com/PaddlePaddle/Serving/blob/develop/doc/Install_CN.md#2.1)
```bash
pip3 install paddle-serving-client==0.9.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip3 install paddle-serving-app==0.9.0 -i https://pypi.tuna.tsinghua.edu.cn/simple

# CPU Server
pip3 install paddle-serving-server==0.9.0 -i https://pypi.tuna.tsinghua.edu.cn/simple

# GPU Server，需要确认环境再选择执行哪一条，推荐使用CUDA 11.2的包
pip3 install paddle-serving-server-gpu==0.9.0.post112 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 1.3 环境检查
```bash
# 安装paddlepaddle
python -m pip install paddlepaddle-gpu==2.3.2.post112 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html
# 
pip3 install https://paddle-inference-lib.bj.bcebos.com/2.3.0/python/Linux/GPU/x86-64_gcc8.2_avx_mkl_cuda11.2_cudnn8.2.1_trt8.0.3.4/paddlepaddle_gpu-2.3.0.post112-cp36-cp36m-linux_x86_64.whl

# 检查
python3 -m paddle_serving_server.serve check
```



# 2 使用

## 2.1 http服务

* [Paddle Serving 快速开始示例](https://github.com/PaddlePaddle/Serving/blob/v0.9.0/doc/Quick_Start_CN.md)

```bash
cd Serving/examples/C++/fit_a_line

python3 -m paddle_serving_server.serve --model uci_housing_model --thread 10 --port 9299

curl -H "Content-Type:application/json" -X POST -d '{"feed":[{"x": [0.0137, -0.1136, 0.2553, -0.0692, 0.0582, -0.0727, -0.1583, -0.0584, 0.6283, 0.4919, 0.1856, 0.0795, -0.0332]}], "fetch":["price"]}' http://127.0.0.1:9299/uci/prediction
```


## 2.2 Pipeline服务

```bash
# get model
python3 -m paddle_serving_app.package --get_model ocr_rec
tar -xzvf ocr_rec.tar.gz
python3 -m paddle_serving_app.package --get_model ocr_det
tar -xzvf ocr_det.tar.gz

# get dataset
wget --no-check-certificate https://paddle-serving.bj.bcebos.com/ocr/test_imgs.tar
tar xf test_imgs.tar

# run services
python3 web_service.py &>log.txt &

python3 pipeline_http_client.py
```
