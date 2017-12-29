
v1
```
python2 classify.py \
    ../examples/images/cat.jpg \
    opf.npy \
    --model_def ../models/bvlc_googlenet/deploy.prototxt \
    --pretrained_model ../models/bvlc_googlenet/bvlc_googlenet.caffemodel \
    --mean_file caffe/imagenet/ilsvrc_2012_mean.npy \
    --center_only
```

v2
```
python2 classify.py \
    ../examples/images/cat.jpg \
    opf.npy \
    --model_def /Users/zhangxin/data_public/goolenet/caffe/InceptionBN-21K-for-Caffe/deploy.prototxt \
    --pretrained_model /Users/zhangxin/data_public/goolenet/caffe/InceptionBN-21K-for-Caffe/Inception21k.caffemodel \
    --mean_file caffe/imagenet/ilsvrc_2012_mean.npy \
    --images_dim 395,395
```

v3
```
python2 classify.py \
    ../examples/images/cat.jpg \
    opf.npy \
    --model_def /Users/zhangxin/data_public/goolenet/caffe/inception-v3/deploy_inception-v3.prototxt \
    --pretrained_model /Users/zhangxin/data_public/goolenet/caffe/inception-v3/inception-v3.caffemodel \
    --mean_file caffe/imagenet/ilsvrc_2012_mean.npy \
    --images_dim 395,395
```


v4
```
python2 classify.py \
    ../examples/images/cat.jpg \
    opf.npy \
    --model_def /Users/zhangxin/data_public/goolenet/caffe/inception-v4/deploy_inception-v4.prototxt \
    --pretrained_model /Users/zhangxin/data_public/goolenet/caffe/inception-v4/inception-v4.caffemodel \
    --mean_file caffe/imagenet/ilsvrc_2012_mean.npy \
    --images_dim 299,299
```

resnet-v2
```
python2 classify.py \
    ../examples/images/cat.jpg \
    opf.npy \
    --model_def /Users/zhangxin/data_public/goolenet/caffe/inception-resnet-v2/deploy_inception-resnet-v2.prototxt \
    --pretrained_model /Users/zhangxin/data_public/goolenet/caffe/inception-resnet-v2/inception-resnet-v2.caffemodel \
    --mean_file caffe/imagenet/ilsvrc_2012_mean.npy \
    --images_dim 331,331
```