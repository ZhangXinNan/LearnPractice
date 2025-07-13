
import jieba
from simhash import Simhash

words1 = jieba.lcut('我很想要打游戏，但是女朋友会生气！', cut_all=True)
words2 = jieba.lcut('我很想要打游戏，但是女朋友非常生气！', cut_all=True)
print(words1)
print(words2)



print(Simhash(words1).distance(Simhash(words2)))

