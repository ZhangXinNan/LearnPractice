#coding=utf-8


# Sequential模型如下
from keras.models import Sequential

model = Sequential()

#将一些网络层通过.add()堆叠起来
from keras.layers import Dense, Activation

model.add(Dense(output_dim=64, input_dim=100))
model.add(Activation("relu"))
model.add(Dense(output_dim=10))
model.add(Activation("softmax"))

# 完成模型的搭建后，我们需要使用.compile()方法来编译模型：
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
# 编译模型时必须指明损失函数和优化器，如果你需要的话，也可以自己定制损失函数。
# Keras的一个核心理念就是简明易用同时，保证用户对Keras的绝对控制力度，用户可以根据自己的需要定制自己的模型、网络层，甚至修改源代码。
# from keras.optimizers import SGD
# model.compile(loss='categorical_crossentropy', optimizer=SGD(lr=0.01, momentum=0.9, nesterov=True))

# 完成模型编译后，我们在训练数据上按batch进行一定次数的迭代训练，以拟合网络，关于为什么要使用‘batch’，请参考一些基本概念
model.fit(X_train, Y_train, nb_epoch=5, batch_size=32)

# 当然，我们也可以手动将一个个batch的数据送入网络中训练，这时候需要使用：
model.train_on_batch(X_batch, Y_batch)

# 随后，我们可以使用一行代码对我们的模型进行评估，看看模型的指标是否满足我们的要求：
loss_and_metrics = model.evaluate(X_test, Y_test, batch_size=32)
# 或者，我们可以使用我们的模型，对新的数据进行预测：
classes = model.predict_classes(X_test, batch_size=32)
proba = model.predict_proba(X_test, batch_size=32)

# 搭建一个问答系统、图像分类模型，或神经图灵机、word2vec词嵌入器就是这么快。
# 支撑深度学习的基本想法本就是简单的，现在让我们把它的实现也变的简单起来！