
# 1. 安装
## 1.1 安装PaddlePaddle
```bash
# GPU cuda
pip install paddlepaddle-gpu
# CPU
pip install paddlepaddle
```

## 1.2 安装PaddleOCR whl包
```bash
pip install paddleocr
```

# 2. 便捷使用
## 2.1 命令行使用
### 2.1.1 中英文模型
检测+方向分类器+识别全流程：--use_angle_cls true设置使用方向分类器识别180度旋转文字，--use_gpu false设置不使用GPU
```bash
paddleocr --image_dir ./imgs/11.jpg --use_angle_cls true --use_gpu false

# 单独使用检测：设置--rec为false
paddleocr --image_dir ./imgs/11.jpg --rec false

# 单独使用识别：设置--det为false
paddleocr --image_dir ./imgs_words/ch/word_1.jpg --det false
```

### 2.1.2 多语言模型

## 2.2 Python脚本使用
### 2.2.1 中英文与多语言使用
```python
from paddleocr import PaddleOCR, draw_ocr

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
img_path = './imgs/11.jpg'
result = ocr.ocr(img_path, cls=True)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)

# 显示结果
from PIL import Image
result = result[0]
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
im_show = Image.fromarray(im_show)
im_show.save('result.jpg')
```

# 3.小结