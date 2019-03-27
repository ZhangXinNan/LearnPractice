


```
[----------] 4 tests from CuDNNDeconvolutionLayerTest/2, where TypeParam = caffe::GPUDevice<float>
[ RUN      ] CuDNNDeconvolutionLayerTest/2.TestSimpleCuDNNDeconvolution
F0327 11:50:10.866304 26661 cudnn_deconv_layer.cpp:53] Check failed: status == CUDNN_STATUS_SUCCESS (4 vs. 0)  CUDNN_STATUS_INTERNAL_ERROR
*** Check failure stack trace: ***
    @     0x7fb44cb185cd  google::LogMessage::Fail()
    @     0x7fb44cb1a433  google::LogMessage::SendToLog()
    @     0x7fb44cb1815b  google::LogMessage::Flush()
    @     0x7fb44cb1ae1e  google::LogMessageFatal::~LogMessageFatal()
    @     0x7fb44adef78b  caffe::CuDNNDeconvolutionLayer<>::LayerSetUp()
    @           0x4926af  caffe::Layer<>::SetUp()
    @           0x62f89d  caffe::CuDNNDeconvolutionLayerTest_TestSimpleCuDNNDeconvolution_Test<>::TestBody()
    @           0x95a3b3  testing::internal::HandleExceptionsInMethodIfSupported<>()
    @           0x9539ca  testing::Test::Run()
    @           0x953b18  testing::TestInfo::Run()
    @           0x953bf5  testing::TestCase::Run()
    @           0x954ecf  testing::internal::UnitTestImpl::RunAllTests()
    @           0x9551f3  testing::UnitTest::Run()
    @           0x4712ed  main
    @     0x7fb44a116830  __libc_start_main
    @           0x479299  _start
    @              (nil)  (unknown)
Makefile:542: recipe for target 'runtest' failed
make: *** [runtest] Aborted (core dumped)

```


解决方法：
```
```