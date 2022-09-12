

import os
import cv2
from paddleocr import PPStructure,save_structure_res

table_engine = PPStructure(table=False, ocr=False, show_log=True)


ppocr_dir = '/Users/zhangxin/github/PaddleOCR/'
save_folder = './output'
img_path = os.path.join(ppocr_dir, 'ppstructure/docs/table/1.png')
img = cv2.imread(img_path)
result = table_engine(img)
save_structure_res(result, save_folder, os.path.basename(img_path).split('.')[0])

for i, line in enumerate(result):
    roi_img = line.pop('img')
    cv2.imwrite(os.path.join(save_folder, "{}_{}.jpg".format(i, line['type'])), roi_img)
    print(i, line)




