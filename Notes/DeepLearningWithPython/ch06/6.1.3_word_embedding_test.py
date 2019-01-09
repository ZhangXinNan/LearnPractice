import keras

from keras.layers import Embedding

from keras.datasets import imdb
from keras import preprocessing

from keras.models import Sequential
from keras.layers import Flatten, Dense

import os



from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np

from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense


# 1. 处理IMDB原始数据
imdb_dir = 'D:/data_public/NLP/aclImdb'
train_dir = os.path.join(imdb_dir, 'train')

labels = []
texts = []

# f = open(os.path.join(dir_name, fname))
'''
Traceback (most recent call last):
File "6.1.3_word_embedding.py", line 25, in <module>
texts.append(f.read())
UnicodeDecodeError: 'gbk' codec can't decode byte 0x93 in position 130: illegal multibyte sequence
'''
for label_type in ['neg', 'pos']:
    dir_name = os.path.join(train_dir, label_type)
    for fname in os.listdir(dir_name):
        if fname[-4:] == '.txt':
            f = open(os.path.join(dir_name, fname), 'r', encoding='UTF-8')

            texts.append(f.read())
            f.close()
            if label_type == 'neg':
                labels.append(0)
            else:
                labels.append(1)

maxlen = 100  # We will cut reviews after 100 words
max_words = 10000  # We will only consider the top 10,000 words in the dataset

tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(texts)

imdb_dir = 'D:/data_public/NLP/aclImdb'



embedding_dim = 100

model = Sequential()
model.add(Embedding(max_words, embedding_dim, input_length=maxlen))
model.add(Flatten())
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
print(model.summary())
# 7. 训练模型与评估模型
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['acc'])



test_dir = os.path.join(imdb_dir, 'test')

labels = []
texts = []

for label_type in ['neg', 'pos']:
    dir_name = os.path.join(test_dir, label_type)
    for fname in sorted(os.listdir(dir_name)):
        if fname[-4:] == '.txt':
            f = open(os.path.join(dir_name, fname), 'r', encoding='UTF-8')
            texts.append(f.read())
            f.close()
            if label_type == 'neg':
                labels.append(0)
            else:
                labels.append(1)

sequences = tokenizer.texts_to_sequences(texts)
x_test = pad_sequences(sequences, maxlen=maxlen)
y_test = np.asarray(labels)

model.load_weights('pre_trained_glove_model.h5')
print(model.evaluate(x_test, y_test))


