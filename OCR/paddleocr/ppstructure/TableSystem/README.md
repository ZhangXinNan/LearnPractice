
python3.7 table/predict_table.py \
    --det_model_dir=inference/ch_PP-OCRv3_det_infer \
    --rec_model_dir=inference/ch_PP-OCRv3_rec_infer  \
    --table_model_dir=inference/ch_ppstructure_mobile_v2.0_SLANet_infer \
    --rec_char_dict_path=../ppocr/utils/ppocr_keys_v1.txt \
    --table_char_dict_path=../ppocr/utils/dict/table_structure_dict_ch.txt \
    --image_dir=docs/table/table.jpg \
    --output=../output/table


python3.7 table/predict_table.py \
    --det_model_dir=inference/ch_PP-OCRv3_det_infer \
    --rec_model_dir=inference/ch_PP-OCRv3_rec_infer  \
    --table_model_dir=inference/ch_ppstructure_mobile_v2.0_SLANet_infer \
    --rec_char_dict_path=../ppocr/utils/ppocr_keys_v1.txt \
    --table_char_dict_path=../ppocr/utils/dict/table_structure_dict_ch.txt \
    --image_dir=/Users/zhangxin/data_yx/登记证/高志成/ocr_50_欣哥_prep/830.jpg \
    --output=../output/table



python3.7 table/predict_structure.py \
    --table_model_dir=inference/picodet_lcnet_x1_0_fgd_layout_table_infer \
    --table_char_dict_path=../ppocr/utils/dict/table_structure_dict_ch.txt \
    --image_dir=/Users/zhangxin/data_yx/登记证/高志成/ocr_50_欣哥_prep/830.jpg \
    --output=./output/table



python3 table_test.py --det_model_dir=inference/ch_PP-OCRv3_det_infer \
                          --rec_model_dir=inference/ch_PP-OCRv3_rec_infer \
                          --table_model_dir=inference/ch_ppstructure_mobile_v2.0_SLANet_infer \
                          --image_dir=./docs/table/table.jpg \
                          --rec_char_dict_path=../ppocr/utils/ppocr_keys_v1.txt \
                          --table_char_dict_path=../ppocr/utils/dict/table_structure_dict_ch.txt \
                          --output=../output \
                          --vis_font_path=../doc/fonts/simfang.ttf \
                          --layout=false