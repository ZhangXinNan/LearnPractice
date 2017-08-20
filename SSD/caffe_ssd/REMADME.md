运行make之后出现如下错误：
```
/usr/include/boost/property_tree/detail/json_parser_read.hpp:257:264: error: ‘type name’ declared as function returning an array 
escape 
^ 
/usr/include/boost/property_tree/detail/json_parser_read.hpp:257:264: error: ‘type name’ declared as function returning an array 
make: * [.build_release/cuda/src/caffe/layers/detection_output_layer.o] Error 1 
make: * Waiting for unfinished jobs….
```

办法： 
修改json_parser_read.hpp：打开文件夹Document，选中computer，在搜索json_parser_read.hpp，找到该文件的路径之后用如下命令打开
```
sudo gedit /usr/include/boost/property_tree/detail/json_parser_read.hpp
```
将257行开始的escape代码段注释掉即可，如下：
```
/*escape
                    =   chset_p(detail::widen<Ch>("\"\\/bfnrt").c_str())
                            [typename Context::a_escape(self.c)]
                    |   'u' >> uint_parser<unsigned long, 16, 4, 4>()
                            [typename Context::a_unicode(self.c)]
                    ;*/
```