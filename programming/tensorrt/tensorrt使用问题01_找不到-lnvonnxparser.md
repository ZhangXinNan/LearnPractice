


# 1 问题
```bash
(base) ➜  TensorRT-introduction git:(master) ✗ make clean && make   
rm -f *.engine
rm -f simpleOnnx_1 simpleOnnx simpleOnnx_2 *.o
g++ -std=c++11 -DONNX_ML=1 -Wall -I/usr/local/cuda/include    -c -o simpleOnnx_1.o simpleOnnx_1.cpp
simpleOnnx_1.cpp: In function ‘void verifyOutput(const std::vector<float>&, const std::vector<float>&, int)’:
simpleOnnx_1.cpp:94:26: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     for (size_t i = 0; i < size; ++i)
                        ~~^~~~~~
g++ -std=c++11 -DONNX_ML=1 -Wall -I/usr/local/cuda/include    -c -o ioHelper.o ioHelper.cpp
ioHelper.cpp: In function ‘std::ostream& nvinfer1::operator<<(std::ostream&, nvinfer1::ILogger::Severity)’:
ioHelper.cpp:52:12: warning: enumeration value ‘kVERBOSE’ not handled in switch [-Wswitch]
     switch (severity)
            ^
cc -L/usr/local/cuda/lib64 -L/usr/local/cuda/lib64/stubs -L/usr/local/lib  simpleOnnx_1.o ioHelper.o  -Wl,--start-group -lnvonnxparser -lnvinfer -lcudart_static -lonnx -lonnx_proto -lprotobuf -lstdc++ -lm -lrt -ldl -lpthread -Wl,--end-group -o simpleOnnx_1
/usr/bin/ld: 找不到 -lnvonnxparser
/usr/bin/ld: 找不到 -lnvinfer
collect2: error: ld returned 1 exit status
<内置>: recipe for target 'simpleOnnx_1' failed
make: *** [simpleOnnx_1] Error 1
```


# 解决办法
添加相应的库目录到环境变量中。



