
import os
import cv2
from paddleocr import PPStructure,save_structure_res

table_engine = PPStructure(layout=False, show_log=True)

ppocr_dir = '/Users/zhangxin/github/PaddleOCR/'
save_folder = './output'
img_path = os.path.join(ppocr_dir, 'ppstructure/docs/table/table.jpg')
img = cv2.imread(img_path)
result = table_engine(img)
save_structure_res(result, save_folder, os.path.basename(img_path).split('.')[0])

for i, line in enumerate(result):
    line.pop('img')
    print(i, line)