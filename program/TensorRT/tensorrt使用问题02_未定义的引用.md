
# 1 问题

```
/usr/local/lib/libonnx_proto.a(onnx-ml.pb.cc.o):(.data.rel.ro._ZTVN4onnx18OperatorSetIdProtoE[_ZTVN4onnx18OperatorSetIdProtoE]+0x60)：对‘google::protobuf::Message::CheckTypeAndMergeFrom(google::protobuf::MessageLite const&)’未定义的引用
/usr/local/lib/libonnx_proto.a(onnx-ml.pb.cc.o):(.data.rel.ro._ZTVN4onnx18OperatorSetIdProtoE[_ZTVN4onnx18OperatorSetIdProtoE]+0xa8)：对‘google::protobuf::Message::DiscardUnknownFields()’未定义的引用
/usr/local/lib/libonnx_proto.a(onnx-ml.pb.cc.o):(.data.rel.ro._ZTVN4onnx18OperatorSetIdProtoE[_ZTVN4onnx18OperatorSetIdProtoE]+0xb0)：对‘google::protobuf::Message::SpaceUsed() const’未定义的引用
/usr/local/lib/libonnx_proto.a(onnx-ml.pb.cc.o):(.data.rel.ro._ZTVN4onnx13FunctionProtoE[_ZTVN4onnx13FunctionProtoE]+0x20)：对‘google::protobuf::Message::GetTypeName[abi:cxx11]() const’未定义的引用
/usr/local/lib/libonnx_proto.a(onnx-ml.pb.cc.o):(.data.rel.ro._ZTVN4onnx13FunctionProtoE[_ZTVN4onnx13FunctionProtoE]+0x58)：对‘google::protobuf::Message::InitializationErrorString[abi:cxx11]() const’未定义的引用
/usr/local/lib/libonnx_proto.a(onnx-ml.pb.cc.o):(.data.rel.ro._ZTVN4onnx13FunctionProtoE[_ZTVN4onnx13FunctionProtoE]+0x60)：对‘google::protobuf::Message::CheckTypeAndMergeFrom(google::protobuf::MessageLite const&)’未定义的引用
/usr/local/lib/libonnx_proto.a(onnx-ml.pb.cc.o):(.data.rel.ro._ZTVN4onnx13FunctionProtoE[_ZTVN4onnx13FunctionProtoE]+0xa8)：对‘google::protobuf::Message::DiscardUnknownFields()’未定义的引用
/usr/local/lib/libonnx_proto.a(onnx-ml.pb.cc.o):(.data.rel.ro._ZTVN4onnx13FunctionProtoE[_ZTVN4onnx13FunctionProtoE]+0xb0)：对‘google::protobuf::Message::SpaceUsed() const’未定义的引用
ioHelper.o：在函数‘nvinfer1::readTensorProto(std::string const&, float*)’中：
ioHelper.cpp:(.text+0x184)：对‘google::protobuf::MessageLite::ParseFromString(std::string const&)’未定义的引用
ioHelper.o：在函数‘nvinfer1::readTensor(std::vector<std::string, std::allocator<std::string> > const&, std::vector<float, std::allocator<float> >&)’中：
ioHelper.cpp:(.text+0x305)：对‘google::protobuf::internal::VerifyVersion(int, int, char const*)’未定义的引用
ioHelper.o：在函数‘google::protobuf::internal::GetEmptyStringAlreadyInited()’中：
ioHelper.cpp:(.text._ZN6google8protobuf8internal27GetEmptyStringAlreadyInitedEv[_ZN6google8protobuf8internal27GetEmptyStringAlreadyInitedEv]+0x7)：对‘google::protobuf::internal::empty_string_’未定义的引用
ioHelper.cpp:(.text._ZN6google8protobuf8internal27GetEmptyStringAlreadyInitedEv[_ZN6google8protobuf8internal27GetEmptyStringAlreadyInitedEv]+0x32)：对‘google::protobuf::internal::empty_string_’未定义的引用
collect2: error: ld returned 1 exit status
```

# 2 解决办法

重新编译protobuf


