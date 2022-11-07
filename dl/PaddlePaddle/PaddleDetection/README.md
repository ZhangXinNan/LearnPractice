

[PaddlePaddle/PaddleDetection](https://github.com/PaddlePaddle/PaddleDetection)

# 配置环境
```bash
conda create -n py38_paddle_det python=3.8

conda activate py38_paddle_det

python -m pip install paddlepaddle-gpu==2.3.2.post111 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html

# 克隆PaddleDetection仓库
# cd <path/to/clone/PaddleDetection>
git clone https://github.com/PaddlePaddle/PaddleDetection.git

# 安装其他依赖
cd PaddleDetection
pip install -r requirements.txt

# 编译安装paddledet
python setup.py install
```

# 使用ppyolo训练coco


export CUDA_VISIBLE_DEVICES=1 #windows和Mac下不需要执行该命令
python tools/train.py -c configs/ppyolo/ppyolo_mbv3_small_coco.yml
                        --use_vdl=true \
                        --vdl_log_dir=vdl_dir/scalar \



