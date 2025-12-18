


python3 tools/infer/predict_system.py \
    --image_dir="./doc/imgs/" \
    --draw_img_save_dir="inference_results/" \
    --det_model_dir="./inference/ch_ppocr_mobile_v2.0_det_infer" \
    --rec_model_dir="./inference/ch_ppocr_mobile_v2.0_rec_infer/" \
    --cls_model_dir="./inference/ch_ppocr_mobile_v2.0_cls_infer" \
    --use_angle_cls=True \
    --use_tensorrt=True
