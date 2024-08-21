
python3 tools/infer/predict_rec.py \
    --image_dir="./doc/imgs_words_en/word_10.png" \
    --rec_model_dir="inference/ch_ppocr_mobile_v2.0_rec_infer"

python3 tools/infer/predict_rec.py \
    --image_dir="doc/imgs_words/ch" \
    --rec_model_dir="inference/ch_ppocr_mobile_v2.0_rec_infer"

python3 tools/infer/predict_rec.py --image_dir="./doc/imgs_words_en/word_336.png" --rec_model_dir="./inference/latin_PP-OCRv3_rec_infer" --rec_image_shape="3, 32, 100" --rec_char_dict_path="./ppocr/utils/dict/latin_dict.txt"

