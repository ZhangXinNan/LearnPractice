

[PaddlePaddle/PaddleDetection](https://github.com/PaddlePaddle/PaddleDetection)

# 配置环境
## 安装paddlepaddle
```bash
conda create -n py39_paddledet python=3.9

conda activate py39_paddledet

python -m pip install paddlepaddle-gpu==2.6.1.post112 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html
```
验证是否安装成功
```python
# 在您的Python解释器中确认PaddlePaddle安装成功
import paddle
paddle.utils.run_check()
```

```bash
# 确认PaddlePaddle版本
python -c "import paddle; print(paddle.__version__)"
# 2.6.1
```

## 安装paddledet
```bash
# 克隆PaddleDetection仓库
# cd <path/to/clone/PaddleDetection>
git clone https://github.com/PaddlePaddle/PaddleDetection.git

# 安装其他依赖
cd PaddleDetection
pip install -r requirements.txt

# 编译安装paddledet
python setup.py install
```

```bash
python ppdet/modeling/tests/test_architectures.py
# Ran 7 tests in 2.946s
# 
# OK
```


# 快速体验
```bash
# 在GPU上预测一张图片
export CUDA_VISIBLE_DEVICES=0
python tools/infer.py -c configs/ppyolo/ppyolo_r50vd_dcn_1x_coco.yml -o use_gpu=true weights=https://paddledet.bj.bcebos.com/models/ppyolo_r50vd_dcn_1x_coco.pdparams --infer_img=demo/000000014439.jpg
```

# 使用ppyolo训练coco

```bash
export CUDA_VISIBLE_DEVICES=1 #windows和Mac下不需要执行该命令
python tools/train.py -c configs/ppyolo/ppyolo_mbv3_small_coco.yml
                        --use_vdl=true \
                        --vdl_log_dir=vdl_dir/scalar \
```


