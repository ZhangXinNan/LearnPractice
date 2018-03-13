#encoding=utf8

import paddle.v2 as paddle
import paddle.v2.dataset.uci_housing as uci_housing

# 模型初始化
paddle.init(use_gpu=False, trainer_count=1)


# 数据
x = paddle.layer.data(name='x', type=paddle.data_type.dense_vector(13))
y_predict = paddle.layer.fc(input=x, size=1, act=paddle.activation.Linear())
y = paddle.layer.data(name='y', type=paddle.data_type.dense_vector(1))
# cost = paddle.layer.mse_cost(input=y_predict, label=y)
cost = paddle.layer.square_error_cost(input=y_predict, label=y)

# 参数，优化器，训练器
parameters = paddle.parameters.create(cost)
optimizer = paddle.optimizer.Momentum(momentum=0)
trainer = paddle.trainer.SGD(cost=cost, parameters=parameters, update_equation=optimizer)


