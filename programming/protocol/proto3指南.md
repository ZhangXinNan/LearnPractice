.proto文件的语法，如何生成数据访问类。

```proto
syntax = "proto3";

message ScarchRequest {
    string query = 1;
    int32 page_number = 2;
    int32 result_per_page = 3;
}
```

1. 在首行声明使用proto3。前边不能有空行或者注释。
2. 每个属性有一个唯一的编号。
3. 注释使用//或者/* */，类似于C/C++。

# oneof

# Any




