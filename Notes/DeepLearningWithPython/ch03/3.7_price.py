


import keras

# 加载数据
from keras.datasets import boston_housing

(train_data, train_targets), (test_data, test_targets) =  boston_housing.load_data()

# 数据标准化，减平均值 ，再除以标准差
mean = train_data.mean(axis=0)
train_data -= mean
std = train_data.std(axis=0)
train_data /= std

test_data -= mean
test_data /= std

from keras import models, layers

def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(train_data.shape[1],)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    return model


import numpy as np

k = 4
num_val_samples = len(train_data) // 4
num_epochs = 100
all_scores = []
all_mae_histories = []

for i in range(k):
    print('processing fold #', i)
    b = i * num_val_samples
    e = (i+1) * num_val_samples
    val_data = train_data[b: e]
    val_targets = train_targets[b: e]

    partial_train_data = np.concatenate([train_data[:b], train_data[e:]])
    partial_train_targets = np.concatenate([train_targets[:b], train_targets[e:]])

    model = build_model()
    print(model.summary())
    history = model.fit(partial_train_data, partial_train_targets, epochs = num_epochs, batch_size=1, verbose=0)
    val_mse, val_mae = model.evaluate(val_data, val_targets, verbose=0)
    all_scores.append(val_mae)
    # print(history.history.keys())
    mae_history = history.history['mean_absolute_error'] # val_mean_absolute_error  KeyError: 'val_mean_absolute_error'
    all_mae_histories.append(mae_history)

average_mae_history = [np.mean([x[i] for x in all_mae_histories]) for i in range(num_epochs)]


import matplotlib.pyplot as plt
# plt.plot(range(1, len(average_mae_history) + 1), average_mae_history)
# plt.xlabel('Epochs')
# plt.ylabel('Validation MAE')
# plt.show()

def smooth_curve(points, factor=0.9):
    smoothed_points = []
    for point in points:
        if smoothed_points:
            previous = smoothed_points[-1]
            smoothed_points.append(previous * factor + point * (i-factor))
        else:
            smoothed_points.append(point)
    return smoothed_points


smooth_mae_history = smooth_curve(average_mae_history)
plt.plot(range(1, len(smooth_mae_history) + 1), smooth_mae_history)
plt.xlabel('Epochs')
plt.ylabel('Validation MAE')
plt.show()









