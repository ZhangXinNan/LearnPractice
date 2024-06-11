
# 创建虚拟环境
```bash
conda activate py39_paddleseg
```

# 安装PaddlePaddle
```bash
python -m pip install paddlepaddle-gpu==2.6.1.post112 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html
```

# 安装PaddleSeg

```bash
cd PaddleSeg
pip install -r requirements.txt
pip install -v -e .
```