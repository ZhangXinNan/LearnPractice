
## 2.2 tensorboard和op
### 2.2.1 数据序列化 -events文件
TensorBoard 通过读取events文件来运行，需要将数据生成一个序列化的Summary protobuf对象。

```python
tf.summary.FileWriter("./tmp/tensorflow/summary/test/", graph=sess.graph)
```
这将在指定目录中生成一个events文件，其名称格式如下：
```
events.out.tfevents.{timestamp}.{hostname}
```



### 2.2.2 启动TensorBoard
在浏览器中打开TensoBoard的图页面：127.0.0.1:6006，将会看到。
```bash
tensorboard --logdir="./tmp/tensorflow/summary/test/"
```


### 2.2.3 常用op

类型 | 实例
--|--
标量运算 |  add sub mul div exp log greater less equal 
向量运算 | concat slice splot constant rank shape shuffle
矩阵运算 | matmul matrixinverse matrixdateminant
带状态的运算    | Variable assign assignadd
神经网络组件    | softmax signoid relu convolution max_pool
存储、恢复      | Save Restore
队列及同步运算  | Enqueue Dequeue MutexAcquire MutexRelease
控制流          | Merge Switch Enter Leave NextIteration

操作函数 | 操作对象
--|--
tf.constant(Tensor对象) | Const
tf.add(tensor对象1, tensor对象2) | Add
一般小写 | 一般大写


### op
一个操作对象（Operation）是TensorFlow图中的一个节点，可以接收0个或者多个输入Tensor，并且可以输出0个或者多个Tensor，Operation对象是通过op构造函数创建的。

例如：`c = tf.matmul(a, b)` 创建了一个Operation对象，类型为MatMul类型，它将张量a,b作为输入，c作为输出。

```python
import tensorflow as tf

a = tf.constant(3)
b = tf.constant(4)
c = tf.add(a, b)

print('a:', a)
print('b:', b)
print('c:', c)
```
输出：
```bash
a: Tensor("Const:0", shape=(), dtype=int32)
b: Tensor("Const_1:0", shape=(), dtype=int32)
c: Tensor("Add:0", shape=(), dtype=int32)
```

打印出来的是张量值，每一个OP指令对应一个唯一的名称。
张量名称的形式为：
`<OP_NAME>:<i>`

一个图有一个命名空间。






