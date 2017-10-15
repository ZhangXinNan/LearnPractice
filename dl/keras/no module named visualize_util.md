```
from keras.utils.visualize_util import plot

ImportError: No module named visualize_util
```
出现这种错误，如何解决呢？

这是Keras升级到2后出现的问题，因为接口改变了。

将代码改为：
```
from keras.utils.vis_utils import plot_model
```
原来的plot 更名为 plot_model

测试代码：
```
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import SGD
from keras.utils import np_utils
from keras.utils.vis_utils import plot_model

model = Sequential()
model.add(Dense(4, input_dim=2, init='uniform'))
model.add(Activation('relu'))
model.add(Dense(2, init='uniform'))
model.add(Activation('sigmoid'))

sgd = SGD(lr=0.05, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='binary_crossentropy', optimizer=sgd,metrics=['accuracy'])
plot_model(model, to_file='model.png')
```
结果是生成一个model.png