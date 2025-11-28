
# 1 通用中英文OCR数据集
## 1.1 ICDAR2019-LSVT
- Data sources：https://aistudio.baidu.com/datasetdetail/177210
- Introduction：A total of 45w Chinese street view images, including 5w (2w test + 3w training) fully labeled data (text coordinates + text content), 40w weakly labeled data (text content only), as shown in the following figure:
- (a) Fully labeled data
- (b) Weakly labeled data - Download link：https://ai.baidu.com/broad/download?dataset=lsvt


## 1.2 ICDAR2017-RCTW-17
- Data sources：https://rctw.vlrlab.net/
- Introduction：It contains 12000 + images, most of them are collected in the wild through mobile camera. Some are screenshots. These images show a variety of scenes, including street views, posters, menus, indoor scenes and screenshots of mobile applications.
- Download link：https://rctw.vlrlab.net/dataset/


## 1.3 中文街景文字识别
Chinese Street View Text Recognition
以中文场景文字识别为主题，提供大规模的中文场景文字识别数据，对图像区域中的文字行进行预测，返回文字行的内容。
标签：文字识别比赛时间：2019/07/05 - 2019/10/31

- Data sources：https://aistudio.baidu.com/aistudio/competition/detail/8
- Introduction：A total of 290000 pictures are included, of which 210000 are used as training sets (with labels) and 80000 are used as test sets (without labels). The dataset is collected from the Chinese street view, and is formed by by cutting out the text line area (such as shop signs, landmarks, etc.) in the street view picture. All the images are preprocessed: by using affine transform, the text area is proportionally mapped to a picture with a height of 48 pixels, as shown in the figure:
(a) Label: 魅派集成吊顶
(b) Label: 母婴用品连锁
- Download link https://aistudio.baidu.com/aistudio/datasetdetail/8429


## 1.4 中文文档文字识别
- Data sources：https://github.com/YCG09/chinese_ocr
- Introduction：
  - A total of 3.64 million pictures are divided into training set and validation set according to 99:1.
  - Using Chinese corpus (news + classical Chinese), the data is randomly generated through changes in font, size, grayscale, blur, perspective, stretching, etc.
  - 5990 characters including Chinese characters, English letters, numbers and punctuation（Characters set: https://github.com/YCG09/chinese_ocr/blob/master/train/char_std_5990.txt ）
  - Each sample is fixed with 10 characters, and the characters are randomly intercepted from the sentences in the corpus
  - Image resolution is 280x32
- Download link：https://pan.baidu.com/s/1QkI7kjah8SPHwOQ40rS1Pw (Password: lu7m)


## 1.5 ICDAR2019-ArT
- Data source：https://aistudio.baidu.com/datasetdetail/177206
- Introduction：It includes 10166 images, 5603 in training sets and 4563 in test sets. It is composed of three parts: total text, scut-ctw1500 and Baidu curved scene text, including text with various shapes such as horizontal, multi-directional and curved.
- Download link：https://ai.baidu.com/broad/download?dataset=art

## 1.6 电子印章数据集
- Data source: https://aistudio.baidu.com/aistudio/datasetdetail/154271/0
- Data introduction: Contains 10,000 images in total, 8,000 images in the training set, and 2,000 images in the test set. The dataset is synthesized by a program and does not involve privacy security. It is mainly used for the training and detection of seal curved text. Contributed by developer jingsongliujing
- Download address: https://aistudio.baidu.com/aistudio/datasetdetail/154271/0

## 1.7 参考文献

# 2 手写中文OCR数据集
# 3 垂类多语言OCR数据集
## 3.1 中国城市车牌数据集
## 3.2 银行信用卡数据集
## 3.3 验证码数据集-Captcha
## 3.4 多语言数据集(Multi-lingual scene text detection and recognition)

# 4 版面分析数据集
# 5 表格识别数据集
# 6 关键信息提取数据集