

安装paddlepaddle-gpu
```bash
python3 -m pip install paddlepaddle==1.7.2 -i https://mirror.baidu.com/pypi/simple
python3 -m pip install paddlepaddle-gpu==1.7.2 -i https://mirror.baidu.com/pypi/simple

python -m pip install paddlepaddle-gpu==2.0.0rc0.post101 -f https://paddlepaddle.org.cn/whl/stable.html
```


```bash
x2paddle --framework=caffe \
    --prototxt=/home/zhangxin/gitlab_md/pose-service/data/body_25b/pose_deploy.prototxt \
    --weight=/home/zhangxin/gitlab_md/pose-service/data/body_25b/pose_iter_XXXXXX.caffemodel \
    --save_dir=/home/zhangxin/gitlab_md/pose-service/data/body_25b/pd_model



x2paddle --framework=caffe \
    --prototxt=/home/zhangxin/gitlab_md/pose-service/data/body_25b/pose_deploy.prototxt \
    --weight=/home/zhangxin/gitlab_md/pose-service/data/body_25b/pose_iter_XXXXXX.caffemodel \
    --save_dir=/home/zhangxin/gitlab_md/pose-service/data/body_25b/pd_model_merge \
    --params_merge

# 使用paddlepaddle 2.0时没法转
# You are using Paddle compiled with TensorRT, but TensorRT dynamic library is not found. Ignore this if TensorRT is not needed.paddle.__version__ = 2.0.0-rc0
# [ERROR] paddlepaddle>=1.6.0 is required

```

# hand
```bash
x2paddle --framework=caffe \
    --prototxt=/home/zhangxin/github/openpose-CMU/models/hand/pose_deploy.prototxt \
    --weight=/home/zhangxin/github/openpose-CMU/models/hand/pose_iter_102000.caffemodel \
    --save_dir=/home/zhangxin/gitlab_md/pose-service/data/hand/pd_model_merge \
    --params_merge
```

# body
```bash
x2paddle --framework=caffe \
    --prototxt=/home/zhangxin/github/openpose-CMU/models/pose/body_25/pose_deploy.prototxt \
    --weight=/home/zhangxin/github/openpose-CMU/models/pose/body_25/pose_iter_584000.caffemodel \
    --save_dir=/home/zhangxin/gitlab_md/pose-service/data/body_25/pd_model_merge \
    --params_merge
```


