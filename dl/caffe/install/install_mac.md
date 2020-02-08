# 问题1
## ld: library not found for -llibopencv_stitching.3.3.1.dylib
```
➜  caffe git:(zxdev_mac) make
LD -o .build_release/lib/libcaffe.so.1.0.0
clang: warning: argument unused during compilation: '-pthread' [-Wunused-command-line-argument]
ld: library not found for -llibopencv_stitching.3.3.1.dylib
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make: *** [.build_release/lib/libcaffe.so.1.0.0] Error 1
```

## 解决方法：
```
brew uninstall opencv
brew install opencv
```

# 问题2
## make test时出现error
```
Undefined symbols for architecture x86_64:
  "caffe::DecodeDatum(caffe::Datum*, bool)", referenced from:
      caffe::IOTest_TestDecodeDatum_Test::TestBody() in test_io.o
  "caffe::CVMatToDatum(cv::Mat const&, caffe::Datum*)", referenced from:
      caffe::IOTest_TestCVMatToDatum_Test::TestBody() in test_io.o
      caffe::IOTest_TestCVMatToDatumContent_Test::TestBody() in test_io.o
      caffe::IOTest_TestCVMatToDatumReference_Test::TestBody() in test_io.o
  "caffe::ImageDataLayer<double>::load_batch(caffe::Batch<double>*)", referenced from:
      vtable for caffe::ImageDataLayer<double> in test_image_data_layer.o
  "caffe::ImageDataLayer<double>::ShuffleImages()", referenced from:
      vtable for caffe::ImageDataLayer<double> in test_image_data_layer.o
  "caffe::ImageDataLayer<double>::DataLayerSetUp(std::__1::vector<caffe::Blob<double>*, std::__1::allocator<caffe::Blob<double>*> > const&, std::__1::vector<caffe::Blob<double>*, std::__1::allocator<caffe::Blob<double>*> > const&)", referenced from:
      vtable for caffe::ImageDataLayer<double> in test_image_data_layer.o
  "caffe::ImageDataLayer<double>::~ImageDataLayer()", referenced from:
      vtable for caffe::ImageDataLayer<double> in test_image_data_layer.o
  "caffe::ImageDataLayer<double>::~ImageDataLayer()", referenced from:
      caffe::ImageDataLayerTest_TestRead_Test<caffe::CPUDevice<double> >::TestBody() in test_image_data_layer.o
      caffe::ImageDataLayerTest_TestResize_Test<caffe::CPUDevice<double> >::TestBody() in test_image_data_layer.o
      caffe::ImageDataLayerTest_TestReshape_Test<caffe::CPUDevice<double> >::TestBody() in test_image_data_layer.o
      caffe::ImageDataLayerTest_TestShuffle_Test<caffe::CPUDevice<double> >::TestBody() in test_image_data_layer.o
      caffe::ImageDataLayerTest_TestSpace_Test<caffe::CPUDevice<double> >::TestBody() in test_image_data_layer.o
      vtable for caffe::ImageDataLayer<double> in test_image_data_layer.o
  "caffe::ImageDataLayer<float>::load_batch(caffe::Batch<float>*)", referenced from:
      vtable for caffe::ImageDataLayer<float> in test_image_data_layer.o
  "caffe::ImageDataLayer<float>::ShuffleImages()", referenced from:
      vtable for caffe::ImageDataLayer<float> in test_image_data_layer.o
  "caffe::ImageDataLayer<float>::DataLayerSetUp(std::__1::vector<caffe::Blob<float>*, std::__1::allocator<caffe::Blob<float>*> > const&, std::__1::vector<caffe::Blob<float>*, std::__1::allocator<caffe::Blob<float>*> > const&)", referenced from:
      vtable for caffe::ImageDataLayer<float> in test_image_data_layer.o
  "caffe::ImageDataLayer<float>::~ImageDataLayer()", referenced from:
      vtable for caffe::ImageDataLayer<float> in test_image_data_layer.o
  "caffe::ImageDataLayer<float>::~ImageDataLayer()", referenced from:
      caffe::ImageDataLayerTest_TestRead_Test<caffe::CPUDevice<float> >::TestBody() in test_image_data_layer.o
      caffe::ImageDataLayerTest_TestResize_Test<caffe::CPUDevice<float> >::TestBody() in test_image_data_layer.o
      caffe::ImageDataLayerTest_TestReshape_Test<caffe::CPUDevice<float> >::TestBody() in test_image_data_layer.o
      caffe::ImageDataLayerTest_TestShuffle_Test<caffe::CPUDevice<float> >::TestBody() in test_image_data_layer.o
      caffe::ImageDataLayerTest_TestSpace_Test<caffe::CPUDevice<float> >::TestBody() in test_image_data_layer.o
      vtable for caffe::ImageDataLayer<float> in test_image_data_layer.o
  "caffe::MemoryDataLayer<double>::AddMatVector(std::__1::vector<cv::Mat, std::__1::allocator<cv::Mat> > const&, std::__1::vector<int, std::__1::allocator<int> > const&)", referenced from:
      caffe::MemoryDataLayerTest_AddMatVectorDefaultTransform_Test<caffe::CPUDevice<double> >::TestBody() in test_memory_data_layer.o
      caffe::MemoryDataLayerTest_TestSetBatchSize_Test<caffe::CPUDevice<double> >::TestBody() in test_memory_data_layer.o
      vtable for caffe::MemoryDataLayer<double> in test_memory_data_layer.o
  "caffe::MemoryDataLayer<float>::AddMatVector(std::__1::vector<cv::Mat, std::__1::allocator<cv::Mat> > const&, std::__1::vector<int, std::__1::allocator<int> > const&)", referenced from:
      caffe::MemoryDataLayerTest_AddMatVectorDefaultTransform_Test<caffe::CPUDevice<float> >::TestBody() in test_memory_data_layer.o
      caffe::MemoryDataLayerTest_TestSetBatchSize_Test<caffe::CPUDevice<float> >::TestBody() in test_memory_data_layer.o
      vtable for caffe::MemoryDataLayer<float> in test_memory_data_layer.o
  "caffe::ReadImageToCVMat(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&)", referenced from:
      caffe::IOTest_TestReadImageToDatumContent_Test::TestBody() in test_io.o
      caffe::IOTest_TestReadImageToCVMat_Test::TestBody() in test_io.o
      caffe::IOTest_TestCVMatToDatum_Test::TestBody() in test_io.o
      caffe::IOTest_TestCVMatToDatumContent_Test::TestBody() in test_io.o
      caffe::IOTest_TestCVMatToDatumReference_Test::TestBody() in test_io.o
      caffe::IOTest_TestDecodeDatumToCVMatContent_Test::TestBody() in test_io.o
      caffe::IOTest_TestDecodeDatumToCVMatContentNative_Test::TestBody() in test_io.o
      ...
  "caffe::ReadImageToCVMat(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, bool)", referenced from:
      caffe::IOTest_TestReadImageToDatumContentGray_Test::TestBody() in test_io.o
      caffe::IOTest_TestReadImageToCVMatGray_Test::TestBody() in test_io.o
  "caffe::ReadImageToCVMat(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, int, int)", referenced from:
      caffe::IOTest_TestReadImageToCVMatResized_Test::TestBody() in test_io.o
      caffe::IOTest_TestReadImageToCVMatResizedSquare_Test::TestBody() in test_io.o
  "caffe::ReadImageToCVMat(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, int, int, bool)", referenced from:
      caffe::IOTest_TestReadImageToCVMatResizedGray_Test::TestBody() in test_io.o
  "caffe::ReadImageToDatum(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, int, int, int, bool, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, caffe::Datum*)", referenced from:
      caffe::DBTest<caffe::TypeLevelDB>::SetUp() in test_db.o
      caffe::DBTest<caffe::TypeLMDB>::SetUp() in test_db.o
      caffe::IOTest_TestReadImageToDatum_Test::TestBody() in test_io.o
      caffe::IOTest_TestReadImageToDatumReference_Test::TestBody() in test_io.o
      caffe::IOTest_TestReadImageToDatumReferenceResized_Test::TestBody() in test_io.o
      caffe::IOTest_TestReadImageToDatumContent_Test::TestBody() in test_io.o
      caffe::IOTest_TestReadImageToDatumContentGray_Test::TestBody() in test_io.o
      ...
  "caffe::DecodeDatumNative(caffe::Datum*)", referenced from:
      caffe::IOTest_TestDecodeDatumNative_Test::TestBody() in test_io.o
      caffe::IOTest_TestDecodeDatumNativeGray_Test::TestBody() in test_io.o
  "caffe::DecodeDatumToCVMat(caffe::Datum const&, bool)", referenced from:
      caffe::IOTest_TestDecodeDatumToCVMat_Test::TestBody() in test_io.o
      caffe::IOTest_TestDecodeDatumToCVMatContent_Test::TestBody() in test_io.o
  "void caffe::hdf5_load_nd_dataset<double>(long long, char const*, int, int, caffe::Blob<double>*, bool)", referenced from:
      caffe::HDF5OutputLayerTest_TestForward_Test<caffe::CPUDevice<double> >::TestBody() in test_hdf5_output_layer.o
  "void caffe::hdf5_load_nd_dataset<float>(long long, char const*, int, int, caffe::Blob<float>*, bool)", referenced from:
      caffe::HDF5OutputLayerTest_TestForward_Test<caffe::CPUDevice<float> >::TestBody() in test_hdf5_output_layer.o
  "caffe::DecodeDatumToCVMatNative(caffe::Datum const&)", referenced from:
      caffe::IOTest_TestDecodeDatumToCVMatNative_Test::TestBody() in test_io.o
      caffe::IOTest_TestDecodeDatumToCVMatNativeGray_Test::TestBody() in test_io.o
      caffe::IOTest_TestDecodeDatumToCVMatContentNative_Test::TestBody() in test_io.o
  "non-virtual thunk to caffe::ImageDataLayer<double>::~ImageDataLayer()", referenced from:
      vtable for caffe::ImageDataLayer<double> in test_image_data_layer.o
  "non-virtual thunk to caffe::ImageDataLayer<double>::~ImageDataLayer()", referenced from:
      vtable for caffe::ImageDataLayer<double> in test_image_data_layer.o
  "non-virtual thunk to caffe::ImageDataLayer<float>::~ImageDataLayer()", referenced from:
      vtable for caffe::ImageDataLayer<float> in test_image_data_layer.o
  "non-virtual thunk to caffe::ImageDataLayer<float>::~ImageDataLayer()", referenced from:
      vtable for caffe::ImageDataLayer<float> in test_image_data_layer.o
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make: *** [.build_release/test/test_all.testbin] Error 1

```

## 解决方法：
重新编译

# 问题3
## ImportError: numpy.core.multiarray failed to import
```
RuntimeError: module compiled against API version 0xa but this version of numpy is 0x9
Traceback (most recent call last):
  File "caffe_char_recognize.py", line 15, in <module>
    import cv2
  File "/Users/zhangxin/Library/Python/2.7/lib/python/site-packages/cv2/__init__.py", line 9, in <module>
    from .cv2 import *
ImportError: numpy.core.multiarray failed to import
```

## 解决方法
使用numpy版本不致，参见 [ImportError: numpy.core.multiarray failed to import](https://github.com/tensorflow/tensorflow/issues/559)
```
pip install -U numpy
```

# 问题4
## mac下的错误
```
➜  char_recognize git:(zxdev) python caffe_char_recognize.py \
    --model_def ../../_tmp/train/20170810_6880/deploy.prototxt \
    --chars_file ../../_tmp/train/20170810_6880/char_set.txt \
    --pretrained_model ../../_tmp/train/20170810_6880/lenet_iter_200000.caffemodel \
    --input ../../test/pic/pc1_indiv.txt \
    --input_dir ../../test/pic \
    > 20170810_6880_pc1_20w.log
objc[27840]: Class CaptureDelegate is implemented in both /Users/zhangxin/Library/Python/2.7/lib/python/site-packages/cv2/cv2.so (0x11b64ad50) and /usr/local/opt/opencv/lib/libopencv_videoio.3.3.dylib (0x11238a618). One of the two will be used. Which one is undefined.
objc[27840]: Class CVWindow is implemented in both /Users/zhangxin/Library/Python/2.7/lib/python/site-packages/cv2/cv2.so (0x11b64ada0) and /usr/local/opt/opencv/lib/libopencv_highgui.3.3.dylib (0x1123641e8). One of the two will be used. Which one is undefined.
objc[27840]: Class CVView is implemented in both /Users/zhangxin/Library/Python/2.7/lib/python/site-packages/cv2/cv2.so (0x11b64adc8) and /usr/local/opt/opencv/lib/libopencv_highgui.3.3.dylib (0x112364210). One of the two will be used. Which one is undefined.
objc[27840]: Class CVSlider is implemented in both /Users/zhangxin/Library/Python/2.7/lib/python/site-packages/cv2/cv2.so (0x11b64adf0) and /usr/local/opt/opencv/lib/libopencv_highgui.3.3.dylib (0x112364238). One of the two will be used. Which one is undefined.
[1]    27840 segmentation fault  python caffe_char_recognize.py --model_def  --chars_file  --pretrained_model 

```


## 解决方法
不要使用默认的python


