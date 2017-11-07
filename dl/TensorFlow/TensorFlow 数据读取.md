# 详解tensorflow数据读取机制
## tensorflow读取机制图解
tensorflow使用**文件名队列**+**内存队列**双队列的形式读入文件，可以很好地管理epoch。
## tensorflow读取数据机制的对应函数
文件名队列，我们使用tf.train.string_input_producer函数。这个函数需要传入一个文件名list，系统会自动将它转为一个文件名队列。

```
string_input_producer(
    string_tensor,
    num_epochs=None,
    shuffle=True,
    seed=None,
    capacity=32,
    shared_name=None,
    name=None,
    cancel_op=None
)
```

在tensorflow中，内存队列不需要我们自己建立，我们只需要使用reader对象从文件名队列中读取数据就可以了，具体实现可以参考下面的实战代码。

使用tf.train.start_queue_runners之后，才会启动填充队列的线程。

## 实战代码
```
# 导入tensorflow
import tensorflow as tf 

# 新建一个Session
with tf.Session() as sess:
    # 我们要读三幅图片A.jpg, B.jpg, C.jpg
    filename = ['A.jpg', 'B.jpg', 'C.jpg']
    # string_input_producer会产生一个文件名队列
    filename_queue = tf.train.string_input_producer(filename, shuffle=False, num_epochs=5)
    # reader从文件名队列中读数据。对应的方法是reader.read
    reader = tf.WholeFileReader()
    key, value = reader.read(filename_queue)
    # tf.train.string_input_producer定义了一个epoch变量，要对它进行初始化
    tf.local_variables_initializer().run()
    # 使用start_queue_runners之后，才会开始填充队列
    threads = tf.train.start_queue_runners(sess=sess)
    i = 0
    while True:
        i += 1
        # 获取图片数据并保存
        image_data = sess.run(value)
        with open('read/test_%d.jpg' % i, 'wb') as f:
            f.write(image_data)
```
 
 # Dataset API
 此前，在TensorFlow中读取数据一般有两种方法：
* 使用placeholder读内存中的数据
* 使用queue读硬盘中的数据（关于这种方式，可以参考我之前的一篇文章：十图详解tensorflow数据读取机制）
 ## Dataset API的导入

在TensorFlow 1.3中，Dataset API是放在contrib包中的：
```
tf.contrib.data.Dataset
```

而在TensorFlow 1.4中，Dataset API已经从contrib包中移除，变成了核心API的一员：
```
tf.data.Dataset
```

 # 基本概念：Dataset与Iterator
 
 

# 参考资料
[十图详解tensorflow数据读取机制（附代码）](https://zhuanlan.zhihu.com/p/27238630)
[TensorFlow全新的数据读取方式：Dataset API入门教程](https://zhuanlan.zhihu.com/p/30751039)
