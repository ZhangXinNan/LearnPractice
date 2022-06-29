

# 问题
```bash
/Users/zhangxin/github/caffe/src/caffe/layers/window_data_layer.cpp:293:42: error: use of undeclared identifier 'CV_LOAD_IMAGE_COLOR'
        cv_img = cv::imread(image.first, CV_LOAD_IMAGE_COLOR);
                                         ^
1 error generated.
make[2]: *** [src/caffe/CMakeFiles/caffe.dir/layers/window_data_layer.cpp.o] Error 1
make[1]: *** [src/caffe/CMakeFiles/caffe.dir/all] Error 2
make: *** [all] Error 2
```

# 解决办法
1. 将所有的CV_LOAD_IMAGE_COLOR替换为cv::IMREAD_COLOR
2. 将所有的CV_LOAD_IMAGE_GRAYSCALE替换为cv::IMREAD_GRAYSCALE


