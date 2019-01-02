from __future__ import absolute_import, division, print_function
# 使用tf.keras保存模型
'''
# 安装导入TensorFlow依赖
pip install -q h5py pyyaml
'''

import os

import tensorflow as tf
from tensorflow import keras

tf.__version__

# 获取示例数据集
'''
我们将使用 MNIST 数据集训练模型，以演示如何保存权重。要加快演示运行速度，请仅使用前 1000 个样本
'''
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

train_labels = train_labels[:1000]
test_labels = test_labels[:1000]

train_images = train_images[:1000].reshape(-1, 28 * 28) / 255.0
test_images = test_images[:1000].reshape(-1, 28 * 28) / 255.0


# 定义模型
def create_model():
    model = tf.keras.models.Sequential([
        keras.layers.Dense(512, activation=tf.nn.relu, input_shape=(784,)),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

    model.compile(optimizer=tf.keras.optimizers.Adam(),
                    loss=tf.keras.losses.sparse_categorical_crossentropy,
                    metrics=['accuracy'])
    return model


model = create_model()
print(model.summary())

# 在训练期间保存检查点
'''
tf.keras.callbacks.ModelCheckpoint 是执行此任务的回调。该回调需要几个参数来配置检查点。
'''
checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# Create checkpoint callback
cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)

model = create_model()

model.fit(train_images, train_labels,  epochs = 10,
          validation_data = (test_images,test_labels),
          callbacks = [cp_callback])  # pass callback to training


# 创建一个未经训练的全新模型，并用测试集进行评估
model = create_model()

loss, acc = model.evaluate(test_images, test_labels)
print("Untrained model, accuracy: {:5.2f}%".format(100*acc))


# 从检查点加载权重，重新评估
model.load_weights(checkpoint_path)
loss,acc = model.evaluate(test_images, test_labels)
print("Restored model, accuracy: {:5.2f}%".format(100*acc))
# 1000/1000 [==============================] - 0s 35us/step
# Restored model, accuracy: 87.20%


# 检查点回调选项
checkpoint_path = "training_2/cp-{epoch:04d}.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

cp_callback = tf.keras.callbacks.ModelCheckpoint(
    checkpoint_path, verbose=1, save_weights_only=True,
    # Save weights, every 5-epochs.
    period=5)

model = create_model()
model.fit(train_images, train_labels,
          epochs = 50, callbacks = [cp_callback],
          validation_data = (test_images,test_labels),
          verbose=0)


latest = tf.train.latest_checkpoint(checkpoint_dir)
print(latest)
# 注意：默认的 TensorFlow 格式仅保存最近的 5 个检查点。
# 如果您仅在一台机器上训练模型，则您将有 1 个后缀为 .data-00000-of-00001 的分片

# 手动保存权重
# Save the weights
model.save_weights('./checkpoints/my_checkpoint')

# Restore the weights
model = create_model()
model.load_weights('./checkpoints/my_checkpoint')

loss,acc = model.evaluate(test_images, test_labels)
print("Restored model, accuracy: {:5.2f}%".format(100*acc))


# 保存整个模型
'''
整个模型可以保存到一个文件中，其中包含权重值、模型配置乃至优化器配置。这样，您就可以为模型设置检查点，并稍后从完全相同的状态继续训练，而无需访问原始代码。
技巧可保存以下所有内容：
权重值
模型配置（架构）
优化器配置
'''
model = create_model()

model.fit(train_images, train_labels, epochs=5)

# Save entire model to a HDF5 file
model.save('my_model.h5')

# 从该文件重新创建模型
# Recreate the exact same model, including weights and optimizer.
new_model = keras.models.load_model('my_model.h5')
print(new_model.summary())


# 检查其准确率

loss, acc = new_model.evaluate(test_images, test_labels)
print("Restored model, accuracy: {:5.2f}%".format(100*acc))



