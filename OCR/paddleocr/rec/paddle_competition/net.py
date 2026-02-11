
from paddle.nn import Conv2D, BatchNorm2D, LeakyReLU, MaxPool2D, LSTM, Linear, Dropout
from paddle.vision.models import ResNet, resnet34
from paddle.vision.models.resnet import BottleneckBlock
import paddle
from cfg import cfg

# 定义输入层，shape中第0维使用-1则可以在推理时自由调节batch size
input_define = paddle.static.InputSpec(
    shape=[-1, cfg["input_size"][0], cfg["input_size"][1], cfg["input_size"][2]],
    dtype="float32",
    name="img")

# 定义标签
label_define = paddle.static.InputSpec(
    shape=[-1, cfg["label_max_len"]+1],
    dtype="int32",
    name="label")


class Net(paddle.nn.Layer):
    def __init__(self, mode="train"):
        super().__init__()
        self.mode = mode
        # CNN
        # self.resnet34 = ResNet(BottleneckBlock, 34, -1, False)
        self.resnet = resnet34(True, num_classes=-1, with_pool=False)
        self.linear_1 = Linear(16, 100)
        # RNN
        self.lstm = LSTM(512, 256, direction="bidirectional")
        self.dropout = Dropout()
        self.linear_2 = Linear(512, cfg["classify_num"])


    def forward(self, x):
        # (-1, 3, 48, 256)
        x = self.resnet(x)
        # (-1, 512, 2, 8)
        x = paddle.tensor.flatten(x, 2)
        # (-1, 512, 16)
        x = self.linear_1(x)
        # (-1, 512, 100)
        x = paddle.tensor.transpose(x, [0, 2, 1])
        # (-1, 100, 512)
        x = self.lstm(x)[0]
        # (-1, 100, hidden_size*2)
        x = self.dropout(x)
        x = self.linear_2(x)
        # (-1, 100, 3097)
        # 在计算损失时ctc-loss会自动进行softmax，所以在推理模式中需额外做softmax获取标签概率
        if self.mode == "eval":
            # 输出层 - Shape = (Batch Size, Max label len, Prob)
            x = paddle.nn.functional.softmax(x)
            # 转换为标签
            x = paddle.tensor.argmax(x, axis=-1)
        return x


if __name__ == '__main__':
    # 实例化模型
    model = paddle.Model(Net(), inputs=input_define, labels=label_define)
    model.summary()

