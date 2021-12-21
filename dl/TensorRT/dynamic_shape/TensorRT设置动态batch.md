


# 1 PyTorch 转 TensorRT 模型部署 - Dynamic Shape (Batch Size)
  - 博客：[PyTorch 转 TensorRT 模型部署 - Dynamic Shape (Batch Size) - 附完整代码](https://zhuanlan.zhihu.com/p/387853124)
  - 代码：https://github.com/lihaoxiang1989/Tensorrt-CV/tree/master/python_lib
  - 问题：没有调用示例。


# 2 a simple example to learn tensorrt with dynamic shapes
- 代码：[https://github.com/egbertYeah/simple_tensorrt_dynamic](https://github.com/egbertYeah/simple_tensorrt_dynamic)
- 博客：[【tensorrt之dynamic shapes】](https://blog.csdn.net/hello_dear_you/article/details/120252717)

Dynamic shapes指的是我们可以在runtime（推理）阶段来指定some或者all输入数据的维度，同时，提供C++和Python两种接口。一般需要指定为dynamic的是batch_size这一个维度，使得我们可以根据自己实际情况动态设置batch，而不需要每次都重新生成engine文件。

1. 使用最新的接口创建NetworkDefinition对象

    截止到tensorrt-7.2.2，builder创建NetworkDefinition提供两个接口：createNetwork()和createNetworkV2()，这两者之间区别有两点：1. 后者处理的维度从原来的（C,H,W)变成了（B,C,H,W)即包括了batch_size; 2. 是否支持dynamic shapes.

2. 对于input tensor中dynamic的维度，通过-1来占位这个维度

3. 在build阶段设置一个或多个optimization profiles，用来指定在runtime阶段inputs允许的维度范围，一般设置三个profiles，最小，最大和最优。

通过上述设置，在build阶段就可以生成一个带dynamic shapes的engine文件，然后就是在推理阶段如何使用这个engine。

4. 如何使用带dynamic shapes的engine：

    a. 创建一个execution context，此时的context也是dynamic shapes的；

    b. 将想要设置的input dimension绑定context，那么此时context处理的维度确定了；

    c. 基于这个context进行推理。

