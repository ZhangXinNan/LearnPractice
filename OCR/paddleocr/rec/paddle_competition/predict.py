

import paddle
from cfg import cfg
from net import Net, input_define
from reader_infer import InferReader
from ctc_decode import ctc_decode


char_dict_cache = dict()
with open(cfg["label_list"], "r") as file:
    for line in file.readlines():
        char, idx = line.split("\t")
        char_dict_cache[int(idx.strip("\n"))] = char


# 实例化推理模型
model = paddle.Model(Net(mode="eval"), inputs=input_define)
# 加载训练好的参数模型
model.load(cfg["checkpoint_path"])
# 设置运行环境
model.prepare()


# 加载预测Reader
infer_reader = InferReader(cfg["infer_data_path"])
img_names = infer_reader.get_names()
results = model.predict(infer_reader, batch_size=cfg["batch_size"])
index = 0
for text_batch in results[0]:
    # print(text_batch)
    with open("results.txt", "w") as f:
        f.write("new_name\tvalue\n")
        for prob in text_batch:
            out = ctc_decode(prob, char_dict_cache, blank=cfg["classify_num"]-1)
            f.write(img_names[index] + "\t" + out + "\n")
            index += 1


