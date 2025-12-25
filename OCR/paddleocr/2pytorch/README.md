
# 1 文本检测模型推理
```bash
# v2
python ./tools/infer/predict_det.py --image_dir ./doc/imgs --det_model_path models/ch_ptocr_v2_det_infer.pth --image_dir ./doc/imgs/1.jpg

# v3
python ./tools/infer/predict_det.py --det_model_path models/ch_ptocr_v3_det_infer.pth --image_dir ./doc/imgs/1.jpg

# ppocrv4_det
python ./tools/infer/predict_det.py --image_dir ./doc/imgs/00009282.jpg --det_model_path models/ch_ptocr_v4_det_infer.pth --det_yaml_path ./configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_student.yml

# ppocrv4_det server
python ./tools/infer/predict_det.py --image_dir ./doc/imgs/00009282.jpg --det_model_path models/ch_ptocr_v4_det_server_infer.pth --det_yaml_path ./configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_teacher.yml

# PP-OCRv5
# PP-OCRv5_mobile_det
python ./tools/infer/predict_det.py --det_yaml_path configs/det/PP-OCRv5/PP-OCRv5_mobile_det.yml --det_model_path models/ptocrv5/ptocr_v5_mobile_det.pth --image_dir ./doc/imgs/00009282.jpg
# PP-OCRv5_server_det
python ./tools/infer/predict_det.py --use_gpu false --det_algorithm DB --det_yaml_path configs/det/PP-OCRv5/PP-OCRv5_server_det.yml --det_model_path models/ptocrv5/ptocr_v5_server_det.pth --image_dir ./doc/imgs/00009282.jpg
```


# 2 文本识别模型推理
```bash
# v2
python ./tools/infer/predict_rec.py --image_dir ./doc/imgs_words/ch --rec_model_path models/ch_ptocr_v2_rec_infer.pth

# v3
python ./tools/infer/predict_rec.py --rec_model_path models/ch_ptocr_v3_rec_infer.pth --rec_image_shape 3,48,320 --image_dir ./doc/imgs_words/ch

# ppocrv4_rec
python ./tools/infer/predict_rec.py --image_dir ./doc/imgs_words/ch --rec_model_path models/ch_ptocr_v4_rec_infer.pth --rec_yaml_path ./configs/rec/PP-OCRv4/ch_PP-OCRv4_rec.yml --rec_image_shape='3,48,320'

# ppocrv4_rec server
python ./tools/infer/predict_rec.py --image_dir ./doc/imgs_words/ch --rec_model_path models/ch_ptocr_v4_rec_server_infer.pth --rec_yaml_path ./configs/rec/PP-OCRv4/ch_PP-OCRv4_rec_hgnet.yml --rec_image_shape='3,48,320'

# PP-OCRv5
# PP-OCRv5_mobile_rec
python ./tools/infer/predict_rec.py --rec_yaml_path configs/rec/PP-OCRv5/PP-OCRv5_mobile_rec.yml --rec_image_shape='3,48,320' --rec_char_dict_path ./pytorchocr/utils/dict/ppocrv5_dict.txt --rec_model_path models/ptocrv5/ptocr_v5_mobile_rec.pth --image_dir ./doc/imgs_words/ch

# PP-OCRv5/PP-OCRv5_server_rec
python ./tools/infer/predict_rec.py --use_gpu false --rec_yaml_path configs/rec/PP-OCRv5/PP-OCRv5_server_rec.yml --rec_image_shape='3,48,320' --rec_char_dict_path ./pytorchocr/utils/dict/ppocrv5_dict.txt --rec_model_path models/ptocrv5/ptocr_v5_server_rec.pth --image_dir ./doc/imgs_words/ch
```

