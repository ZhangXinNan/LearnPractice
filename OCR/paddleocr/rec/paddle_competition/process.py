
import os
import pandas as pd
from cfg import cfg

def Q2B(s):
    """全角转半角"""
    inside_code=ord(s)
    if inside_code==0x3000:
        inside_code=0x0020
    else:
        inside_code-=0xfee0
    if inside_code<0x0020 or inside_code>0x7e: #转完之后不是半角字符返回原来的字符
        return s
    return chr(inside_code)

def stringQ2B(s):
    """把字符串全角转半角"""
    return "".join([Q2B(c) for c in s])

def is_chinese(s):
    """判断unicode是否是汉字"""
    for c in s:
        if c < u'\u4e00' or c > u'\u9fa5':
            return False
    return True

def is_number(s):
    """判断unicode是否是数字"""
    for c in s:
        if c < u'\u0030' or c > u'\u0039':
            return False
    return True

def is_alphabet(s):
    """判断unicode是否是英文字母"""
    for c in s:
        if c < u'\u0061' or c > u'\u007a':
            return False
    return True

def del_other(s):
    """判断是否非汉字，数字和小写英文"""
    res = str()
    for c in s:
        if not (is_chinese(c) or is_number(c) or is_alphabet(c)):
            c = ""
        res += c
    return res


# df = pd.read_csv("/home/aistudio/data/train_label.csv", encoding="gbk")
# csv_file = '/media/zhangxin/DATA/data_public/OCR/paddle_competition/train/train_label.csv'
csv_file = "/home/zhangxin/data_public/OCR/paddle_competition/SkLXRq6Q/train_label.csv"
# csv_file = os.path.join(cfg['data_path'], 'train_label.csv')
df = pd.read_csv(csv_file, encoding="gbk")
name, value = list(df.name), list(df.value)
for i, label in enumerate(value):
    # 全角转半角
    label = stringQ2B(label)
    # 大写转小写
    label = "".join([c.lower() for c in label])
    # 删除所有空格符号
    label = del_other(label)
    value[i] = label

# 删除标签为""的行
data = zip(name, value)
data = list(filter(lambda c: c[1]!="", list(data)))
# 保存到work目录
with open(cfg["train_list"], "w") as f:
    for line in data:
        f.write(line[0] + "\t" + line[1] + "\n")

# 记录训练集中最长标签
with open(cfg["train_list"], "r") as f:
    for line in f:
        name, label = line.strip().split("\t")
        if len(label) > cfg["label_max_len"]:
            cfg["label_max_len"] = len(label)

print("label max len: ", cfg["label_max_len"])


