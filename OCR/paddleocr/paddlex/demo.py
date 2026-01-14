from paddlex import create_pipeline

pipeline = create_pipeline(pipeline="OCR")

img_path = '/Users/zhangxin/github/LearnPractice/OCR/paddleocr/imgs/general_ocr_002.png'
output = pipeline.predict(
    input=img_path,
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
)

print(type(output))

for res in output:
    # res.print()
    print(type(res))
    print(res.keys())
    for i in range(len(res['rec_texts'])):
        print(i, res['rec_texts'][i])
        print('\t', res['dt_polys'][i].tolist())
        print('\t', res['rec_polys'][i].tolist())
        print('\t', res['rec_boxes'][i].tolist())
    # res.save_to_img(save_path="./output/")
    # res.save_to_json(save_path="./output/")





