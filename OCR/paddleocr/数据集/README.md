
```bash
conda create -n py310_paddleocr python=3.10

conda activate py310_paddleocr

python -m pip install paddlepaddle-gpu==3.2.2 -i https://www.paddlepaddle.org.cn/packages/stable/cu126/

python -m pip install paddleocr
```

# 1. ICDAR2019-LSVT
```bash
tar -xvf train_full_images_0.tar.gz
tar -xvf train_full_images_1.tar.gz


```


# 2. ICDAR2017-RCTW-17
```bash
cat train_images.zip.001 train_images.zip.002 > train_images.zip

unzip train_images.zip
```


# 3. Chinese Street View Text Recognition


