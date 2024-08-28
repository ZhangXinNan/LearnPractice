
import paddle
import paddle.vision as vision
import paddle.text as text

paddle.__version__


# 四、数据集定义、加载和数据预处理
# 4.1 框架自带数据集使用

print('视觉相关数据集：', paddle.vision.datasets.__all__)
print('自然语言相关数据集：', paddle.text.__all__)

from paddle.vision.transforms import ToTensor
# 训练数据集
train_dataset = vision.datasets.MNIST(mode='train', transform=ToTensor())

# 验证数据集
val_dataset = vision.datasets.MNIST(mode='test', transform=ToTensor())


# 4.2 自定义数据集
from paddle.io import Dataset


class MyDataset(Dataset):
    """
    步骤一：继承paddle.io.Dataset类
    """
    def __init__(self, mode='train'):
        """
        步骤二：实现构造函数，定义数据读取方式，划分训练和测试数据集
        """
        super().__init__()

        if mode == 'train':
            self.data = [
                ['traindata1', 'label1'],
                ['traindata2', 'label2'],
                ['traindata3', 'label3'],
                ['traindata4', 'label4'],
            ]
        else:
            self.data = [
                ['testdata1', 'label1'],
                ['testdata2', 'label2'],
                ['testdata3', 'label3'],
                ['testdata4', 'label4'],
            ]
    
    def __getitem__(self, index):
        """
        步骤三：实现__getitem__方法，定义指定index时如何获取数据，并返回单条数据（训练数据，对应的标签）
        """
        data = self.data[index][0]
        label = self.data[index][1]

        return data, label

    def __len__(self):
        """
        步骤四：实现__len__方法，返回数据集总数目
        """
        return len(self.data)

# 测试定义的数据集
train_dataset_2 = MyDataset(mode='train')
val_dataset_2 = MyDataset(mode='test')

print('=============train dataset=============')
for data, label in train_dataset_2:
    print(data, label)

print('=============evaluation dataset=============')
for data, label in val_dataset_2:
    print(data, label)



# 五、模型组网
# 5.1 Sequential组网
# Sequential形式组网
mnist = paddle.nn.Sequential(
    paddle.nn.Flatten(),
    paddle.nn.Linear(784, 512),
    paddle.nn.ReLU(),
    paddle.nn.Dropout(0.2),
    paddle.nn.Linear(512, 10)
)

# 5.2 SubClass组网
# Layer类继承方式组网
class Mnist(paddle.nn.Layer):
    def __init__(self):
        super().__init__()

        self.flatten = paddle.nn.Flatten()
        self.linear_1 = paddle.nn.Linear(784, 512)
        self.linear_2 = paddle.nn.Linear(512, 10)
        self.relu = paddle.nn.ReLU()
        self.dropout = paddle.nn.Dropout(0.2)

    def forward(self, inputs):
        y = self.flatten(inputs)
        y = self.linear_1(y)
        y = self.relu(y)
        y = self.dropout(y)
        y = self.linear_2(y)

        return y

mnist_2 = Mnist()

# 5.3 模型封装
# 使用GPU训练
# paddle.set_device('gpu')

# 模型封装

## 场景1：动态图模式
## 1.1 为模型预测部署场景进行模型训练
## 需要添加input和label数据描述，否则会导致使用model.save(training=False)保存的预测模型在使用时出错
inputs = paddle.static.InputSpec([-1, 1, 28, 28], dtype='float32', name='input')
label = paddle.static.InputSpec([-1, 1], dtype='int8', name='label')
model = paddle.Model(mnist, inputs, label)

## 1.2 面向实验而进行的模型训练
## 可以不传递input和label信息
# model = paddle.Model(mnist)

## 场景2：静态图模式
# paddle.enable_static()
# paddle.set_device('gpu')
# input = paddle.static.InputSpec([None, 1, 28, 28], dtype='float32')
# label = paddle.static.InputSpec([None, 1], dtype='int8')
# model = paddle.Model(mnist, input, label)


# 5.4 模型可视化
model.summary((1, 28, 28))

paddle.summary(mnist, (1, 28, 28))

# 六、模型训练
# 为模型训练做准备，设置优化器，损失函数和精度计算方式
model.prepare(paddle.optimizer.Adam(parameters=model.parameters()), 
              paddle.nn.CrossEntropyLoss(),
              paddle.metric.Accuracy())


# 启动模型训练，指定训练数据集，设置训练轮次，设置每次数据集计算的批次大小，设置日志格式
model.fit(train_dataset, 
          epochs=5, 
          batch_size=64,
          verbose=1)

model.save('mnist')

# 七、模型评估
result = model.evaluate(val_dataset, verbose=1)


# 八、模型预测
pred_result = model.predict(val_dataset)
print(type(pred_result), len(pred_result))
print(type(pred_result[0]), len(pred_result[0]))


