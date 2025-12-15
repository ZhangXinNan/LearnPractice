
from paddleocr import TextDetection
model = TextDetection(model_name="PP-OCRv5_server_det")
img_path = '/Users/zhangxin/gitlab/ocr_service/test/imgs/screenshot/华泰证券专业版3.png'
# img_path = "general_ocr_001.png"
output = model.predict(img_path, batch_size=1)
print(type(output))
for res in output:
    # res.print()
    print(type(res))
    res.save_to_img(save_path="./output/")
    res.save_to_json(save_path="./output/res.json")


