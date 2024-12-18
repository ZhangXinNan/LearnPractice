

[biubug6/Pytorch_Retinaface](https://github.com/biubug6/Pytorch_Retinaface)

resnet50, mobile0.25


python demo.py \
    --trained_model weights/mobilenet0.25_Final.pth \
    --network mobile0.25 \
    --save_folder ./widerface_evaluate/widerface_txt/ \
    --cpu \
    --dataset_folder /Users/zhangxin/data_public/face/wider/WIDER_val/images \
    --save_image

python demo.py --trained_model weights/mobilenet0.25_Final.pth --network mobile0.25 --save_folder imgs_result/id_phy/test1 --cpu --dataset_folder "C:\gitlab\data_philippine_card\national_id_physical\test1\Philippine Identification Card Physical" --save_image

