# 0 介绍
小数据集上。训练仅用了250张标注图片。MaxF1达到96%。Inference仅95ms每张图片。
与TensorVision后端兼容。
KittiBox
MultiNet


# 1 安装依赖
```
pip install numpy scipy pillow matplotlib commentjson
```
或者
```
pip install -r requirements.txt
```

# 2 安装
## 2.1 克隆仓库
```
git clone https://github.com/MarvinTeichmann/KittiSeg.git
```

## 2.2 初始化子模块
```
git submodule update --init --recursive
```
## 2.3 下载道路数据
### 2.3.1 手动下载
```
wget http://www.cvlibs.net/download.php?file=data_road.zip
```
### 2.3.2 自动下载
```
python download_data.py --kitti_url URL_YOU_RETRIEVED
```

## 2.4 注意：只运行demo.py的话不需要下载道路数据。2.3仅是你需要训练自己的模型时才必要。推荐使用2.3.2下载数据，这会自动提取和准备数据。


# 3 教程
## 3.1 入门
```
python demo.py --input_image data/demo/demo.png
python evaluate.py
python train.py --hypes hypes/KittiSeg.json
```

如果你想理解代码，建议先看demo.py。作者已经在每一步写了说明。

## 3.2 数据存储管理
默认数据存储在KittiSeg/DATA下，运行的输出存储在 KittiSeg/RUNS。
可以来通过修改$TV_DIR_DATA and $TV_DIR_RUNS改变存储路径。

## 3.3 RUNDIR 和 实验组织
