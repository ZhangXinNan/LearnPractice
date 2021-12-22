
import paddle


# 定义多层感知机
class MultilayerPerceptron(paddle.nn.Layer):
    def __init__(self, in_features):
        super(MultilayerPerceptron, self).__init__()
        # 形状变换，将数据形状从 [] 变为 []
        self.flatten = paddle.nn.Flatten()
        # 第一个全连接层
        self.linear1 = paddle.nn.Linear(in_features=in_features, out_features=100)
        # 使用ReLU激活函数
        self.act1 = paddle.nn.ReLU()
        # 第二个全连接层
        self.linear2 = paddle.nn.Linear(in_features=100, out_features=100)
        # 使用ReLU激活函数
        self.act2 = paddle.nn.ReLU()
        # 第三个全连接层
        self.linear3 = paddle.nn.Linear(in_features=100, out_features=10)

    def forward(self, x):
        # x = x.reshape((-1, 1, 28, 28))
        x = self.flatten(x)
        x = self.linear1(x)
        x = self.act1(x)
        x = self.linear2(x)
        x = self.act2(x)
        x = self.linear3(x)
        return x