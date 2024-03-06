

# download text angle class inference model：
wget  https://paddleocr.bj.bcebos.com/dygraph_v2.0/ch/ch_ppocr_mobile_v2.0_cls_infer.tar
tar xf ch_ppocr_mobile_v2.0_cls_infer.tar

python3 tools/infer/predict_cls.py --image_dir="./doc/imgs_words/ch" --cls_model_dir="./inference/ch_ppocr_mobile_v2.0_cls_infer"
