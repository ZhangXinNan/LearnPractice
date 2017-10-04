
简单来说容器是镜像的一个运行实例。所不同的是，镜像是静态的只读文件，而容器带有运行时需要的可写入文件层。

## 4.1 创建容器
### 4.1.1 新建容器
```
docker create -it ubuntu:latest 
```
docker create 命令创建的容器处于集上状态，可以使用docker start 命令来启动它。

### 4.1.2 启动容器
```
docker start af
```
启动一个已经创建的容器
```
docker ps
```
查看一个运行中的容器

### 4.1.3 新建并启动容器
除了创建容器后通过start命令来启动，也可以直接新建并启动容器。
```
docker run ubuntu /bin/echo 'Hello World'
```


启动一个bash终端，允许用户进行交互 
```
docker run -it ubuntu:14.04 /bin/bash
```
* -t 让Docker分配一个伪终端并绑定到容器的标准输入上。
* -i 让容器的标准输入保持的模型。

### 4.1.4 守护态运行
添加*-d* 参数 ，让Docker容器在后台以守护态形式运行。

## 4.2 终止容器
```
docker stop [-t|--time[=10]] [CONTAINER...]
```

## 4.3 进入容器
使用-d参数时，容器启动后会进入后台，用户无法看到容器中的信息，也无法进行操作。
### 4.3.1 attach命令
多个容器同时用attach命令连到同一个容器时，所有窗口都会同步显示。当某个窗口阻塞时，其他窗口也无法执行操作了。

### 4.3.2 exec命令
可以在容器内执行任意命令。
```
docker exec -it 243c32535da7 /bin/bash
```

### 4.3.3 nsenter工具

## 4.4 删除容器
docker rm 命令只能删除处于终止或者退出 状态的容器，并不能删除还牌运行状态的容器。

## 4.5 导入和导出容器
### 4.5.1 导出容器
docker export 
### 4.5.2 导入容器
docker import 

## 参考资料
《Docker技术入门与实践》