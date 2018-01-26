# 第3章 TensorFlow基础

## 3.1 数据流图简介

### 3.1.1 数据流图基础
数据流图本质是一组连接在一起的函数。

节点(node)：代表运算或者某种操作。
边(edge)：Operation传入或传出的实际数值。

### 3.1.2 节点的依赖关系



## 3.2 在TensorFlow 中定义数据流图
（1）定义数据流图
（2）运行数据流图（在数据上）

### 3.2.1 构建第一个TensorFlow数据流图
数据流图中的每一个节点称为一个Operation(op)。

```
tensorboard --logdir=./mygraph
```
### 3.2.2 张量思维
### 3.2.3 张量的形状
### 3.2.4 Operation
### 3.2.5 Graph对象
为方便起见，当TensorFlow库被加载时，它会自动创建一个Graph对象，并将其作为默认的数据流图。
### 3.2.6 Session
Session负责数据流图的执行。
构造方法：tf.Session()可接收3个可选参数：
* target 所要使用的执行引擎
* graph 在Session对象中加载的Graph对象
* config 指定配置Session对象的选项。

Session.run()计算所期望的Tensor对象的输出。
* fetches 接收任意的数据流图元素。
* feed_dict 覆盖数据流图中的Tensor对象值

### 3.2.7 利用占位节点添加输入
### 3.2.8 Variable对象

## 3.3 通过名称作用域组织数据流图


## 3.4 练习：综合运用各种组件




