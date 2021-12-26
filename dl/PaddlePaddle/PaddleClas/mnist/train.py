

import paddle
from paddle.vision.transforms import Normalize
import paddle.nn.functional as F
from mlp import MultilayerPerceptron
from lenet import LeNet
from eval import eval

print(paddle.__version__)
print(paddle.utils.run_check())


# 加载训练集 batch_size 设为 64
def train(model, optim, epochs):
    # 用Adam作为优化函数
    for epoch in range(epochs):
        model.train()
        epoch_loss = 0
        epoch_acc = 0
        epoch_num = 0
        for batch_id, data in enumerate(train_loader()):
            x_data = data[0]
            y_data = data[1]
            predicts = model(x_data)
            loss = F.cross_entropy(predicts, y_data)
            # 计算损失
            acc = paddle.metric.accuracy(predicts, y_data)
            loss.backward()
            '''
            if batch_id % 300 == 0:
                print("epoch: {}, batch_id: {}, loss is: {}, acc is: {}".format(epoch, batch_id, loss.numpy(), acc.numpy()))
            '''
            optim.step()
            optim.clear_grad()
            epoch_num += predicts.shape[0]
            epoch_acc += acc.numpy() * predicts.shape[0]
            epoch_loss += loss.numpy() * predicts.shape[0]
        epoch_acc /= epoch_num
        epoch_loss /= epoch_num
        val_acc, val_loss, val_num = eval(model, test_loader)
        print("epoch: {}, train-acc: {}, train-loss: {}, val-acc: {}, val_loss: {}".format(epoch, epoch_acc, epoch_loss, val_acc, val_loss))


transform = Normalize(mean=[127.5],
                               std=[127.5],
                               data_format='CHW')
# 使用transform对数据集做归一化
print('download training data and load training data')
train_dataset = paddle.vision.datasets.MNIST(mode='train', transform=transform)
test_dataset = paddle.vision.datasets.MNIST(mode='test', transform=transform)
print('load finished')


train_loader = paddle.io.DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = paddle.io.DataLoader(test_dataset, places=paddle.CPUPlace(), batch_size=64)
# 使用 paddle.Model 封装 MultilayerPerceptron
# model = paddle.Model(MultilayerPerceptron(in_features=784))
# model = paddle.Model(LeNet())
model = LeNet()
# 使用 summary 打印模型结构
paddle.Model(model).summary((-1, 1, 28, 28))

# 使用Adam算法进行优化
optim = paddle.optimizer.Adam(learning_rate=0.001, parameters=model.parameters())
# 配置模型
'''
model.prepare(optim,
              paddle.nn.CrossEntropyLoss(), # 使用CrossEntropyLoss 计算损失
              paddle.metric.Accuracy()) # 使用Accuracy 计算精度

# 开始模型训练
model.fit(train_dataset, # 设置训练数据集
          epochs=5,      # 设置训练轮数
          batch_size=64, # 设置 batch_size
          verbose=1)     # 设置日志打印格式
'''

epochs = 5
optim = paddle.optimizer.Adam(learning_rate=0.001, parameters=model.parameters())
train(model, optim, epochs)
paddle.save(model.state_dict(), 'lenet.pdparams')


'''
val_result = model.evaluate(test_dataset, verbose=1)
print(val_result)
'''
# test(model)





