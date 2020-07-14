代码地址：[PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)

# 1 中文测试
```bash
python3 tools/infer/predict_rec.py \
    --image_dir doc/imgs_words/ch \
    --rec_model_dir inference/ch_rec_mv3_crnn \
    --rec_image_shaoe "3, 32, 320" \
    --rec_char_type ch \
    --rec_batch_num 30 \
    --rec_algorithm CRNN \
    --rec_char_dict_path ./ppocr/utils/ppocr_keys_v1.txt
```

原效果：
```
Predicts of doc/imgs_words/ch/word_5.jpg:['西湾监管', 0.9652789]
Predicts of doc/imgs_words/ch/word_4.jpg:['实力活力', 0.94463724]
Predicts of doc/imgs_words/ch/word_3.jpg:['电话：15952301928', 0.99584234]
Predicts of doc/imgs_words/ch/word_2.jpg:['汉阳鹦鹉家居建材市场E区25-26号', 0.95212066]
Predicts of doc/imgs_words/ch/word_1.jpg:['韩国小馆', 0.98803014]
Total predict time for 5 images:0.106
```

改进效果：
```
Predicts of doc/imgs_words/ch/word_5.jpg:['西湾监管', 0.9652789]
Predicts of doc/imgs_words/ch/word_4.jpg:['实力活力', 0.94463724]
Predicts of doc/imgs_words/ch/word_3.jpg:['电话：15952301928', 0.99584234]
Predicts of doc/imgs_words/ch/word_2.jpg:['汉阳鹦鹉家居建材市场E区25-26号', 0.95212066]
Predicts of doc/imgs_words/ch/word_1.jpg:['韩国小馆', 0.98803014]
Total predict time for 5 images:0.103
```

# 2 英文测试
```bash
python3 tools/infer/predict_rec.py \
    --image_dir doc/imgs_words_en \
    --rec_model_dir inference/ch_rec_mv3_crnn \
    --rec_image_shaoe "3, 32, 320" \
    --rec_char_type en \
    --rec_batch_num 30 \
    --rec_algorithm CRNN \
    --rec_char_dict_path ./ppocr/utils/ppocr_keys_v1.txt

```

原效果：
```
Predicts of doc/imgs_words_en/word_116.png:['QBhon', 0.60810107]
Predicts of doc/imgs_words_en/word_461.png:['烟国', 0.46494332]
Predicts of doc/imgs_words_en/word_52.png:['Fute', 0.6243137]
Predicts of doc/imgs_words_en/word_201.png:['HOUSE', 0.99250346]
Predicts of doc/imgs_words_en/word_401.png:['lna', 0.5072811]
Predicts of doc/imgs_words_en/word_19.png:['SLOW', 0.8475923]
Predicts of doc/imgs_words_en/word_545.png:['佳', 0.08702037]
Predicts of doc/imgs_words_en/word_10.png:['PAIN', 0.9786783]
Predicts of doc/imgs_words_en/word_308.png:['LITTLE', 0.9917827]
Predicts of doc/imgs_words_en/word_336.png:['6OPER', 0.6035349]
Total predict time for 10 images:0.060
```

改进效果：
```
Predicts of doc/imgs_words_en/word_116.png:['QBhon', 0.60810107]
Predicts of doc/imgs_words_en/word_461.png:['烟国', 0.46494332]
Predicts of doc/imgs_words_en/word_52.png:['Fute', 0.6243137]
Predicts of doc/imgs_words_en/word_201.png:['HOUSE', 0.99250346]
Predicts of doc/imgs_words_en/word_401.png:['lna', 0.5072811]
Predicts of doc/imgs_words_en/word_19.png:['SLOW', 0.8475923]
Predicts of doc/imgs_words_en/word_545.png:['佳', 0.08702037]
Predicts of doc/imgs_words_en/word_10.png:['PAIN', 0.9786783]
Predicts of doc/imgs_words_en/word_308.png:['LITTLE', 0.9917827]
Predicts of doc/imgs_words_en/word_336.png:['6OPER', 0.6035349]
Total predict time for 10 images:0.060
```
