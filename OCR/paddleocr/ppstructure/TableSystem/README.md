


python3 table_test.py --det_model_dir=inference/ch_PP-OCRv3_det_infer \
                          --rec_model_dir=inference/ch_PP-OCRv3_rec_infer \
                          --table_model_dir=inference/ch_ppstructure_mobile_v2.0_SLANet_infer \
                          --image_dir=./docs/table/table.jpg \
                          --rec_char_dict_path=../ppocr/utils/ppocr_keys_v1.txt \
                          --table_char_dict_path=../ppocr/utils/dict/table_structure_dict_ch.txt \
                          --output=../output \
                          --vis_font_path=../doc/fonts/simfang.ttf \
                          --layout=false