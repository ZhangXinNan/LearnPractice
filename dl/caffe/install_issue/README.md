

```angular2html
zhangxin@zhangxin-AW:/media/zhangxin/Data/github/caffe$ make runtest -j8
.build_release/tools/caffe
.build_release/tools/caffe: /home/zhangxin/anaconda3/lib/libtiff.so.5: no version information available (required by /usr/lib/x86_64-linux-gnu/libopencv_imgcodecs.so.3.2)
.build_release/tools/caffe: /home/zhangxin/anaconda3/lib/libtiff.so.5: no version information available (required by /usr/lib/libgdal.so.20)
.build_release/tools/caffe: /home/zhangxin/anaconda3/lib/libtiff.so.5: no version information available (required by /usr/lib/x86_64-linux-gnu/libpoppler.so.73)
.build_release/tools/caffe: /home/zhangxin/anaconda3/lib/libtiff.so.5: no version information available (required by /usr/lib/x86_64-linux-gnu/libgeotiff.so.2)
.build_release/tools/caffe: symbol lookup error: .build_release/tools/caffe: undefined symbol: _ZN5caffe3NetIfE21CopyTrainedLayersFromERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE
Makefile:542: recipe for target 'runtest' failed
make: *** [runtest] Error 127
```

