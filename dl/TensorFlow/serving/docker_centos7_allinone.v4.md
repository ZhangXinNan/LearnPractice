### 拉取镜像
```
# 查看已有镜像
docker image ls
docker pull dhub.data.autohome.com.cn/deeplearning/centos7-allinone:latest
```

### 运行docker
```
docker run --name=allinone_car \
           --device=/dev/nvidia1:/dev/nvidia0 \
           --device=/dev/nvidiactl:/dev/nvidiactl \
           --device=/dev/nvidia-uvm:/dev/nvidia-uvm \
           -i -t \
           -v /data/zhangxin/dockervolume:/root/.cache:rw \
           -v /var/lib/nvidia-docker/volumes/nvidia_driver/367.48:/usr/local/nvidia \
           -p 19100:19100 \
           dhub.data.autohome.com.cn/deeplearning/centos7-allinone:latest /bin/bash
```

### 下载模型

### 切到serving目录下，转换模型到tensorflow_serving
```
cd /serving

bazel-bin/tensorflow_serving/example/inception_saved_model --checkpoint_dir=/root/.cache/zhouhui --output_dir=/root/.cache/zhouhui_out
```


### 启动服务
```
bazel-bin/tensorflow_serving/model_servers/tensorflow_model_server --port=9000 --model_name=inception --model_base_path=/root/.cache/export &> inception_log &
```


### 测试其服务
```
bazel-bin/tensorflow_serving/example/inception_client --server=127.0.0.1:9000 --image=/root/.cache/pic/car.jpg
```


### 启动接口层
```
cd m_tensorflow_client
nohup python service_recog.py > nohup0.out 2>&1 &
```


### 编译
```
清理环境	
bazel clean --expunge && export TF_NEED_CUDA=1
serving目录下编译	
bazel build -c opt --config=cuda tensorflow_serving/...
```

### 进入docker 容器
docker attach zx_tf_test

