
from paddleocr import PaddleOCR

ocr = PaddleOCR()  # need to run only once to download and load model into memory
# img_path = '/home/aistudio/work/word_19.png'
img_path = 'word_19.png'
result = ocr.ocr(img_path, det=False)
for line in result:
    print(line)
