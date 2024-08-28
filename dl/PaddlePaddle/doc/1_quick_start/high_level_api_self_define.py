


# 6.1 单机单卡
# 使用GPU训练
# paddle.set_device('gpu')

# 构建模型训练用的Model，告知需要训练哪个模型
model = paddle.Model(mnist)

# 为模型训练做准备，设置优化器，损失函数和精度计算方式
model.prepare(paddle.optimizer.Adam(parameters=model.parameters()), 
              paddle.nn.CrossEntropyLoss(),
              paddle.metric.Accuracy())

# 启动模型训练，指定训练数据集，设置训练轮次，设置每次数据集计算的批次大小，设置日志格式
model.fit(train_dataset, 
          epochs=5, 
          batch_size=64,
          verbose=1)


# 6.2 自定义Loss
class SelfDefineLoss(paddle.nn.Layer):
    """
    1. 继承paddle.nn.Layer
    """
    def __init__(self):
        """
        2. 构造函数根据自己的实际算法需求和使用需求进行参数定义即可
        """
        super().__init__()

    def forward(self, input, label):
        """
        3. 实现forward函数，forward在调用时会传递两个参数：input和label
            - input：单个或批次训练数据经过模型前向计算输出结果
            - label：单个或批次训练数据对应的标签数据

            接口返回值是一个Tensor，根据自定义的逻辑加和或计算均值后的损失
        """
        # 使用Paddle中相关API自定义的计算逻辑
        # output = xxxxx
        # return output


class SoftmaxWithCrossEntropy(paddle.nn.Layer):
    def __init__(self):
        super().__init__()

    def forward(self, input, label):
        loss = F.softmax_with_cross_entropy(input, 
                                            label, 
                                            return_softmax=False,
                                            axis=1)
        return paddle.mean(loss)


# 6.3 自定义Metric

class SelfDefineMetric(paddle.metric.Metric):
    """
    1. 继承paddle.metric.Metric
    """
    def __init__(self):
        """
        2. 构造函数实现，自定义参数即可
        """
        super().__init__()

    def name(self):
        """
        3. 实现name方法，返回定义的评估指标名字
        """
        return '自定义评价指标的名字'

    def compute(self, ...)
        """
        4. 本步骤可以省略，实现compute方法，这个方法主要用于`update`的加速，可以在这个方法中调用一些paddle实现好的Tensor计算API，编译到模型网络中一起使用低层C++ OP计算。
        """

        return 自己想要返回的数据，会做为update的参数传入。

    def update(self, ...):
        """
        5. 实现update方法，用于单个batch训练时进行评估指标计算。
        - 当`compute`类函数未实现时，会将模型的计算输出和标签数据的展平作为`update`的参数传入。
        - 当`compute`类函数做了实现时，会将compute的返回结果作为`update`的参数传入。
        """
        return acc value
    
    def accumulate(self):
        """
        6. 实现accumulate方法，返回历史batch训练积累后计算得到的评价指标值。
        每次`update`调用时进行数据积累，`accumulate`计算时对积累的所有数据进行计算并返回。
        结算结果会在`fit`接口的训练日志中呈现。
        """
        # 利用update中积累的成员变量数据进行计算后返回
        return accumulated acc value

    def reset(self):
        """
        7. 实现reset方法，每个Epoch结束后进行评估指标的重置，这样下个Epoch可以重新进行计算。
        """
        # do reset action

# 6.4 自定义Callback
class SelfDefineCallback(paddle.callbacks.Callback):
    """
    1. 继承paddle.callbacks.Callback
    2. 按照自己的需求实现以下类成员方法：
        def on_train_begin(self, logs=None)                 训练开始前，`Model.fit`接口中调用
        def on_train_end(self, logs=None)                   训练结束后，`Model.fit`接口中调用
        def on_eval_begin(self, logs=None)                  评估开始前，`Model.evaluate`接口调用
        def on_eval_end(self, logs=None)                    评估结束后，`Model.evaluate`接口调用
        def on_test_begin(self, logs=None)                  预测测试开始前，`Model.predict`接口中调用
        def on_test_end(self, logs=None)                    预测测试结束后，`Model.predict`接口中调用 
        def on_epoch_begin(self, epoch, logs=None)          每轮训练开始前，`Model.fit`接口中调用 
        def on_epoch_end(self, epoch, logs=None)            每轮训练结束后，`Model.fit`接口中调用 
        def on_train_batch_begin(self, step, logs=None)     单个Batch训练开始前，`Model.fit`和`Model.train_batch`接口中调用
        def on_train_batch_end(self, step, logs=None)       单个Batch训练结束后，`Model.fit`和`Model.train_batch`接口中调用
        def on_eval_batch_begin(self, step, logs=None)      单个Batch评估开始前，`Model.evalute`和`Model.eval_batch`接口中调用
        def on_eval_batch_end(self, step, logs=None)        单个Batch评估结束后，`Model.evalute`和`Model.eval_batch`接口中调用
        def on_test_batch_begin(self, step, logs=None)      单个Batch预测测试开始前，`Model.predict`和`Model.test_batch`接口中调用
        def on_test_batch_end(self, step, logs=None)        单个Batch预测测试结束后，`Model.predict`和`Model.test_batch`接口中调用
    """
    def __init__(self):
        super().__init__()

    # 按照需求定义自己的类成员方法


class ModelCheckpoint(Callback):
    def __init__(self, save_freq=1, save_dir=None):
        self.save_freq = save_freq
        self.save_dir = save_dir

    def on_epoch_begin(self, epoch=None, logs=None):
        self.epoch = epoch

    def _is_save(self):
        return self.model and self.save_dir and ParallelEnv().local_rank == 0

    def on_epoch_end(self, epoch, logs=None):
        if self._is_save() and self.epoch % self.save_freq == 0:
            path = '{}/{}'.format(self.save_dir, epoch)
            print('save checkpoint at {}'.format(os.path.abspath(path)))
            self.model.save(path)

    def on_train_end(self, logs=None):
        if self._is_save():
            path = '{}/final'.format(self.save_dir)
            print('save checkpoint at {}'.format(os.path.abspath(path)))
            self.model.save(path)

