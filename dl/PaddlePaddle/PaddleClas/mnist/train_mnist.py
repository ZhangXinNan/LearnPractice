

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
train_dataset = paddle.vision.datasets.MNIST(mode='train', transform=transform)
test_dataset = paddle.vision.datasets.MNIST(mode='test', transform=transform)
print('load finished')

# 使用 paddle.Model 封装 MultilayerPerceptron
# model = paddle.Model(MultilayerPerceptron(in_features=784))
model = paddle.Model(LeNet())
# 使用 summary 打印模型结构
model.summary((-1, 1, 28, 28))


# 配置模型
model.prepare(paddle.optimizer.Adam(parameters=model.parameters()),  # 使用Adam算法进行优化
              paddle.nn.CrossEntropyLoss(), # 使用CrossEntropyLoss 计算损失
              paddle.metric.Accuracy()) # 使用Accuracy 计算精度

# 开始模型训练
model.fit(train_dataset, # 设置训练数据集
          epochs=5,      # 设置训练轮数
          batch_size=64, # 设置 batch_size
          verbose=1)     # 设置日志打印格式

val_result = model.evaluate(test_dataset, verbose=1)
print(val_result)







