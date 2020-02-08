Docker服务器配置指南
# 1.安装Docker
https://docs.docker.com/install/linux/docker-ce/centos/
1）Install required packages
yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
2）set up the stable repository
yum-config-manager \
    --add-repo \
https://download.docker.com/linux/centos/docker-ce.repo
3）Install the latest version of Docker CE
yum install docker-ce
4）Start Docker
systemctl start docker

# 2.安装Nvidia-docker2
https://github.com/NVIDIA/nvidia-docker
1）Add the package repositories
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.repo | \
  sudo tee /etc/yum.repos.d/nvidia-docker.repo
2）Install nvidia-docker2 and reload the Docker daemon configuration
yum install -y nvidia-docker2
pkill -SIGHUP dockerd

# 3.安装Nvidia驱动
1）下载驱动
https://www.nvidia.cn/Download/index.aspx?lang=cn
Tesla -> P-series -> Tesla P100 -> Linux 64-bit
2）如遇到kernel相关错误，下载kernel devel并安装
http://vault.centos.org/7.4.1708/updates/x86_64/Packages

# 4.服务器Docker设置
1）设置默认Root Dir
修改/etc/systemd/system/docker.service.d/docker.root.conf（如不存在，新建）
增加如下内容。（如将Root Dir修改为/diskb/docker）
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -g /diskb/docker
运行docker info 查看Docker Root Dir是否修改成功。
2）从原服务器上迁移image
保存镜像：docker save -o 要保存的文件名 要保存的镜像
载入镜像：docker load < 文件名
3）新增镜像
如：docker pull nvidia/cuda:9.0-cudnn7-runtime
https://hub.docker.com/r/nvidia/cuda/
注：新增镜像后，需安装openssh-server服务并开启，并提交为新镜像。
apt install openssh-server
修改Root登陆权限：
vim /etc/ssh/sshd_config
将PermitRootLogin prohibit-password改为PermitRootLogin yes
打开ssh服务
service ssh start


# 5.新增用户
运行create_container.py
参数：
  --name NAME        container名称，通常使用用户名字拼音
  --image IMAGE       加载的镜像名，如xp-pytorch-caffe:ssh，可通过docker images查看
  --port-num PORT_NUM  【可选】额外开放的端口数量，默认为9。

成功生成后将随机产生密码，通过root用户及密码进行ssh登陆。


# 6. 参考资料
[NVIDIA/nvidia-docker](https://github.com/NVIDIA/nvidia-docker)

