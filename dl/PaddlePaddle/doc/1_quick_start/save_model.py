
import paddle
import paddle.nn.functional as F
from paddle.nn import Layer
from paddle.vision.datasets import MNIST
from paddle.metric import Accuracy
from paddle.nn import Conv2D,MaxPool2D,Linear
from paddle.static import InputSpec
from paddle.vision.transforms import ToTensor

print(paddle.__version__)



# 三、数据集
train_dataset = MNIST(mode='train', transform=ToTensor())
test_dataset = MNIST(mode='test', transform=ToTensor())


# 四、模型组建
class MyModel(Layer):
    def __init__(self):
        super().__init__()
        self.conv1 = paddle.nn.Conv2D(in_channels=1, out_channels=6, kernel_size=5, stride=1, padding=2)
        self.max_pool1 = MaxPool2D(kernel_size=2, stride=2)
        self.conv2 = Conv2D(in_channels=6, out_channels=16, kernel_size=5, stride=1)
        self.max_pool2 = MaxPool2D(kernel_size=2, stride=2)
        self.linear1 = Linear(in_features=16*5*5, out_features=120)
        self.linear2 = Linear(in_features=120, out_features=84)
        self.linear3 = Linear(in_features=84, out_features=10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.max_pool1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = self.max_pool2(x)
        x = paddle.flatten(x, start_axis=1, stop_axis=-1)
        x = self.linear1(x)
        x = F.relu(x)
        x = self.linear2(x)
        x = F.relu(x)
        x = self.linear3(x)
        return x


# 五、模型训练
inputs = InputSpec([None, 784], 'float32', 'x')
labels = InputSpec([None, 10], 'float32', 'x')
model = paddle.Model(MyModel(), inputs, labels)

optim = paddle.optimizer.Adam(learning_rate=0.001, parameters=model.parameters())

model.prepare(
    optim,
    paddle.nn.CrossEntropyLoss(),
    Accuracy()
    )
'''
model.fit(train_dataset,
        test_dataset,
        epochs=3,
        batch_size=64,
        save_dir='mnist_checkpoint',
        verbose=1
        )
'''


# 六、保存模型参数
'''
paddle 高阶API-模型参数保存
* paddle.Model.fit          只能保存模型参数，不能保存优化器参数
* paddle.Model.save         可以保存模型结构、网络参数和优化器参数

paddle 基础框架-动态图-模型参数保存
* paddle.save

paddle 基础框架-静态图-模型参数保存
* paddle.static.save
* paddle.static.save_inference_model

'''
# 方法一：训练过程中实时保存每个epoch的模型参数
model.fit(train_dataset,
        test_dataset,
        epochs=2,
        batch_size=64,
        save_dir='mnist_checkpoint',
        verbose=1
        )

# 方法二：model.save()保存模型和优化器参数信息
model.save('mnist_checkpoint/test')


# 七、加载模型参数

'''
高阶API-模型参数加载
* paddle.Model.load
model.load能够同时加载模型和优化器参数。
通过reset_optimizer参数来指定是否需要恢复优化器参数，
若reset_optimizer参数为True，则重新初始化优化器参数，
若reset_optimizer参数为False，则从路径中恢复优化器参数。


paddle 基础框架-动态图-模型参数加载
* paddle.load

paddle 基础框架-静态图-模型参数加载
* paddle.io.load 
* paddle.io.load_inference_model

'''


# 八、恢复训练

import paddle
from paddle.vision.datasets import MNIST
from paddle.metric import Accuracy
from paddle.static import InputSpec

train_dataset = MNIST(mode='train', transform=ToTensor())
test_dataset = MNIST(mode='test', transform=ToTensor())

inputs = InputSpec([None, 784], 'float32', 'inputs')
labels = InputSpec([None, 10], 'float32', 'labels')
model = paddle.Model(MyModel(), inputs, labels)
optim = paddle.optimizer.Adam(learning_rate=0.001, parameters=model.parameters())
# model.load("./mnist_checkpoint/final")
model.load("./mnist_checkpoint/test", reset_optimizer=False)
model.prepare( 
      optim,
      paddle.nn.loss.CrossEntropyLoss(),
      Accuracy()
      )
model.fit(train_data=train_dataset,
        eval_data=test_dataset,
        batch_size=64,
        epochs=2,
        verbose=1
        )
