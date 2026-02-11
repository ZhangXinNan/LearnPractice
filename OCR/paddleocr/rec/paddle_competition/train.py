
import paddle
from net import Net, input_define, label_define
from cfg import cfg
from ctc_loss import CTCLoss
from reader import Reader


# 打包图片和标签
train_data = list()
with open(cfg["train_list"], "r") as f:
    next(f)
    for line in f:
        img_name, label = line.strip().split("\t")
        train_data.append([img_name, label])
print(cfg['train_list'], len(train_data))

# 实例化模型
model = paddle.Model(Net(), inputs=input_define, labels=label_define)
model.summary()

# 定义优化器
optimizer = paddle.optimizer.Adam(learning_rate=cfg["learning_rate"], parameters=model.parameters())

# 为模型配置运行环境并设置该优化策略
model.prepare(
    optimizer=optimizer,
    loss=CTCLoss())

# 执行训练
model.fit(
    train_data=Reader(train_data),
    eval_data=Reader(train_data, is_val=True),
    batch_size=cfg["batch_size"],
    epochs=cfg["epoch"],
    save_dir=cfg["save_dir"],
    save_freq=10,
    log_freq=1,
    verbose=1)


