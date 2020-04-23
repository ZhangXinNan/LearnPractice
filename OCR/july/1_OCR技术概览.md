

OCR (Optical Character Recognition) 光学字符识别。

# 一 OCR的典型应用场景
1. 票证识别：身份证、发票、驾驶证、银行卡、名片。
2. 车牌识别：停车场（固定位置、车速减慢）、道路（车速快）
3. 拍照搜题：单题（要求框选单题）、多题、拍照检查
4. 自然场景：交通标志、路边门牌
5. 内容审核：短视频、视频
6. 内容理解：

# 二 常见难点
1. 复杂版式
2. 扭曲形变
3. 笔迹干扰、手写、涂改
4. 不均匀光照、反光、弱光
5. 失焦、运动模糊、摩尔纹
6. 复杂背景
7. 多字体、多语言混排
8. 角度、弯曲、变形
9. 表格

ICDAR2019  challenge

# 三 OCR基本流程
1. 预处理
2. 版面分析
3. 文本行定位
4. 字符分割识别
5. 后处理

## 3.0 预处理
1. 降噪：滤波、光照处理
2. 增强：灰度拉伸
3. 二值化：由灰度图像变为二值图像
4. 倾斜校正：HOUGH变换、投影法



## 3.1 实例一 通用文本识别
distance measure between Connected Components
1. minimum run-length (MRL) distance 每一行里CC1与CC2的最小距离
2. euclidean distance between gravity centers (ECC) 两个重心 的距离

ovlp 两个连通域的overlap重叠部分的高度
h1,h2 两个连通域自己的高度
vdc  两个重心垂直距离
span 两个连通域高的并集


最小生成树


字符分割：
1. 投影法
2. 维特比

预处理：
1. OTSU
2. MSER





## 3.2 实例二 车牌识别







