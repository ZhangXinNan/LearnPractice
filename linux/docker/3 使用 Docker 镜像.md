

Docker运行前需要本地存在对应的镜像，如果镜像没保存在本地，Docker会尝试先从默认镜像仓库下载，用户也可以通过配置，使用自定义的镜像仓库。

## 3.1 获取镜像
```
docker pull Name[:tag]
```
其中Name是镜像仓库的名称（用来区分镜像），TAG是镜像的标签（往往用来表示版本信息）。

* 不指定TAG，会默认使用latest标签。
* 下载过程中可以看出，镜像文件一般由若干层(layer)组成。
* 严格地讲，镜像的仓库名称还应该添加仓库地址。

```
docker pull ubuntu:14.04
```
相当于从默认的注册服务器Docker Hub Registry中的ubuntu仓库下载标记为14.04的镜像。即：
```
docker pull registry.hub.docker.com/ubuntu:14.04
```

## 3.2 查看镜像信息
*docker image* 命令列出本地主机上已有镜像的基本信息。
*docker tag* 在本地镜像添加新的标签。
*docker inspect* 获取 镜像的详细信息。
*docker history* 查看镜像的历史信息。

## 3.3 搜寻镜像
*docker search* 搜索远端仓库中共享的镜像

## 3.4 删除镜像
### 3.4.1 使用标签删除镜像
```
docker rmi IMAGE [Image ...]
```
只删除标签，不一定影响镜像。
### 3.4.2 使用镜像id删除镜像
先深度删除所有指向该镜像的标签，再删除镜像本身。
不推荐使用-f强行删除镜像。先删除依赖该镜像的所有容器，再来删除镜像。


## 3.5 创建镜像
### 3.5.1 基于已有镜像的容器创建
```
docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]
```

### 3.5.2 基于本地模板导入

### 3.5.3 基于Dockerfile 创建

## 3.6 存出和载入镜像
### 3.6.1 存出镜像
```
docker save
```
### 3.6.2 载入镜像
```
docker load
```

### 3.7 上传镜像
```
docker push NAME[:TAG] | [REGISTRY_HOST[:REGISTRY_PORT]/]NAME[:TAG]
```

## 参考资料
【Docker技术入门与实践】