
import paddle
import paddle.nn.functional as F
import numpy as np

print(paddle.__version__)


# 二、基本用法
# 在动态图模式下，你可以直接运行一个飞桨提供的API，它会立刻返回结果到python。不再需要首先创建一个计算图，然后再给定数据去运行。
a = paddle.randn([4, 2])
b = paddle.arange(1, 3, dtype='float32')

print(a)
print(b)

c = a + b
print(c)

d = paddle.matmul(a, b)
print(d)

# 三、使用python的控制流
# 动态图模式下，你可以使用python的条件判断和循环，这类控制语句来执行神经网络的计算。（不再需要cond, loop这类OP)

a = paddle.to_tensor(np.array([1, 2, 3]))
b = paddle.to_tensor(np.array([4, 5, 6]))

for i in range(10):
    r = paddle.rand([1,])
    if r > 0.5:
        c = paddle.pow(a, i) + b
        print("{} +> {}".format(i, c.numpy()))
    else:
        c = paddle.pow(a, i) - b
        print("{} -> {}".format(i, c.numpy()))


# 四、构建更加灵活的网络：控制流
'''
使用动态图可以用来创建更加灵活的网络，比如根据控制流选择不同的分支网络，和方便的构建权重共享的网络。接下来来看一个具体的例子，在这个例子中，第二个线性变换只有0.5的可能性会运行。

在sequence to sequence with attention的机器翻译的示例中，你会看到更实际的使用动态图构建RNN类的网络带来的灵活性。
'''
class MyModel(paddle.nn.Layer):
    def __init__(self, input_size, hidden_size):
        super().__init__()
        self.linear1 = paddle.nn.Linear(input_size, hidden_size)
        self.linear2 = paddle.nn.Linear(hidden_size, hidden_size)
        self.linear3 = paddle.nn.Linear(hidden_size, 1)

    def forward(self, inputs):
        x = self.linear1(inputs)
        x = F.relu(x)

        if paddle.rand([1,]) > 0.5: 
            x = self.linear2(x)
            x = F.relu(x)

        x = self.linear3(x)
        
        return x     

total_data, batch_size, input_size, hidden_size = 1000, 64, 128, 256

x_data = np.random.randn(total_data, input_size).astype(np.float32)
y_data = np.random.randn(total_data, 1).astype(np.float32)

model = MyModel(input_size, hidden_size)

loss_fn = paddle.nn.MSELoss(reduction='mean')
optimizer = paddle.optimizer.SGD(learning_rate=0.01, 
                                 parameters=model.parameters())

for t in range(200 * (total_data // batch_size)):
    idx = np.random.choice(total_data, batch_size, replace=False)
    x = paddle.to_tensor(x_data[idx,:])
    y = paddle.to_tensor(y_data[idx,:])
    y_pred = model(x)

    loss = loss_fn(y_pred, y)
    if t % 200 == 0:
        print(t, loss.numpy())

    loss.backward()
    optimizer.step()
    optimizer.clear_grad()


# 五、构建更加灵活的网络：共享权重
'''
使用动态图还可以更加方便的创建共享权重的网络，下面的示例展示了一个共享了权重的简单的AutoEncoder。

你也可以参考图像搜索的示例看到共享参数权重的更实际的使用。
'''
inputs = paddle.rand((256, 64))

linear = paddle.nn.Linear(64, 8, bias_attr=False)
loss_fn = paddle.nn.MSELoss()
optimizer = paddle.optimizer.Adam(0.01, parameters=linear.parameters())

for i in range(10):
    hidden = linear(inputs)
    # weight from input to hidden is shared with the linear mapping from hidden to output
    outputs = paddle.matmul(hidden, linear.weight, transpose_y=True) 
    loss = loss_fn(outputs, inputs)
    loss.backward()
    print("step: {}, loss: {}".format(i, loss.numpy()))
    optimizer.step()
    optimizer.clear_grad()




