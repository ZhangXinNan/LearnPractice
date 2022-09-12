
import os
import cv2
from paddleocr import PPStructure,draw_structure_result,save_structure_res

table_engine = PPStructure(show_log=True)


ppocr_dir = os.path.join(os.getenv('HOME'), 'github/PaddleOCR/')
save_folder = './output'
img_path = os.path.join(ppocr_dir, 'ppstructure/docs/table/1.png')
img = cv2.imread(img_path)
result = table_engine(img)
save_structure_res(result, save_folder,os.path.basename(img_path).split('.')[0])

for i, line in enumerate(result):
    # line.pop('img')
    roi_img = line.pop('img')
    cv2.imwrite(os.path.join(save_folder, "{}_{}.jpg".format(i, line['type'])), roi_img)
    print(i, line)

from PIL import Image

font_path = os.path.join(ppocr_dir, 'doc/fonts/simfang.ttf') # font provieded in PaddleOCR
image = Image.open(img_path).convert('RGB')
im_show = draw_structure_result(image, result,font_path=font_path)
im_show = Image.fromarray(im_show)
im_show.save('result.jpg')

