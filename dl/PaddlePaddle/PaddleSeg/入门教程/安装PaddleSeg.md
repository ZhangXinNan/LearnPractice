
# 2 本地安装说明
## 2.0 创建虚拟环境
```bash
conda activate py39_paddleseg
```

## 2.1 安装PaddlePaddle
```bash
python -m pip install paddlepaddle-gpu==2.6.1.post112 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html
```

## 2.2 安装PaddleSeg

### 2.2.1 从源码安装
```bash
cd PaddleSeg
pip install -r requirements.txt
pip install -v -e .
```

## 2.3 确认环境安装成功
```bash
sh tests/install/check_predict.sh
```

