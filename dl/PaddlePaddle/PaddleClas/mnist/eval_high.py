


import paddle
from paddle.vision.transforms import Normalize
from mlp import MultilayerPerceptron
from lenet import LeNet


print(paddle.__version__)
print(paddle.utils.run_check())


transform = Normalize(mean=[127.5],
                               std=[127.5],
                               data_format='CHW')
# 使用transform对数据集做归一化
print('download training data and load training data')
# train_dataset = paddle.vision.datasets.MNIST(mode='train', transform=transform)
test_dataset = paddle.vision.datasets.MNIST(mode='test', transform=transform)
print('load finished')


# model = paddle.Model(LeNet())
# model.load('lenet_mnist.pdparams')
model = LeNet()
model.set_state_dict(paddle.load('lenet_mnist.pdparams'))
model = paddle.Model(model)
val_result = model.evaluate(test_dataset, verbose=1)
print(val_result)

