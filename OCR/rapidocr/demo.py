

from rapidocr import RapidOCR

# 步骤2中的1.yaml
config_path = "default_repidocr.yaml"
engine = RapidOCR(config_path=config_path)

img_url = "https://img1.baidu.com/it/u=3619974146,1266987475&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=516"
result = engine(img_url)
print(result)

result.vis("vis_result.jpg")



