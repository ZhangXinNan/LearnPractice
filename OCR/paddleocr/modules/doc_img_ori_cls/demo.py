
import os
import argparse
from paddleocr import DocImgOrientationClassification


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='../imgs/general_ocr_002.png')
    return parser.parse_args()


args = get_args()
model = DocImgOrientationClassification(model_name="PP-LCNet_x1_0_doc_ori")
output = model.predict(args.input,  batch_size=1)
for res in output:
    res.print(json_format=False)
    res.save_to_img("./output/demo.png")
    res.save_to_json("./output/res.json")




