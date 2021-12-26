


import paddle
from paddle.vision.transforms import Normalize
from mlp import MultilayerPerceptron
from lenet import LeNet
import paddle.nn.functional as F


# 加载测试数据集
def eval(model, test_loader):
    total_acc = 0
    total_loss = 0
    total_num = 0
    model.eval()
    for batch_id, data in enumerate(test_loader()):
        x_data = data[0]
        y_data = data[1]
        predicts = model(x_data)
        # print(type(predicts), predicts.shape[0])
        # 获取预测结果
        loss = F.cross_entropy(predicts, y_data)
        acc = paddle.metric.accuracy(predicts, y_data)
        total_acc += acc.numpy() * predicts.shape[0]
        total_loss += loss.numpy() * predicts.shape[0]
        total_num += predicts.shape[0]
        '''
        if batch_id % 20 == 0:
            print("batch_id: {}, loss is: {}, acc is: {}".format(batch_id, loss.numpy(), acc.numpy()))
        '''
    return total_acc / total_num, total_loss / total_num, total_num


if __name__ == '__main__':
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
    test_loader = paddle.io.DataLoader(test_dataset, places=paddle.CPUPlace(), batch_size=64)

    model = LeNet()
    # model.set_state_dict(paddle.load('lenet_mnist.pdparams'))
    model.set_state_dict(paddle.load('lenet.pdparams'))
    val_acc, val_loss, val_num = eval(model, test_loader)
    print("val-acc : {}, val-loss : {}, val-num : {}".format(val_acc, val_loss, val_num))
