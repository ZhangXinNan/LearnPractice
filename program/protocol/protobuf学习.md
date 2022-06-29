
# 1 关于简单例子的描述
我打算使用 Protobuf 和 C++ 开发一个十分简单的例子程序。

该程序由两部分组成。第一部分被称为 Writer，第二部分叫做 Reader。

Writer 负责将一些结构化的数据写入一个磁盘文件，Reader 则负责从该磁盘文件中读取结构化数据并打印到屏幕上。

准备用于演示的结构化数据是 HelloWorld，它包含两个基本数据：
* ID，为一个整数类型的数据
* Str，这是一个字符串


# 2 书写 .proto 文件

```
package lm;
message helloworld
{
  required int32        id = 1;
  required string       str = 2;
  optional int32        opt = 3;
}
```

# 3 编译 .proto 文件
```
protoc lm.helloworld.proto --cpp_out ./
```
命令将生成两个文件：
* lm.helloworld.pb.h ， 定义了 C++ 类的头文件
* lm.helloworld.pb.cc ， C++ 类的实现文件

在生成的头文件中，定义了一个 C++ 类 helloworld，后面的 Writer 和 Reader 将使用这个类来对消息进行操作。诸如对消息的成员进行赋值，将消息序列化等等都有相应的方法。

# 4 编写 writer 和 Reader
## 测试文件Writer
```c++
#include <ios>
#include <fstream>
#include "lm.helloworld.pb.h"
using namespace std;

int main(void)
{
    lm::helloworld msg1;
    msg1.set_id(101);
    msg1.set_str(“hello”);

    // Write the new address book back to disk. 
    fstream output("./log", ios::out | ios::trunc | ios::binary);
            
    if (!msg1.SerializeToOstream(&output)) { 
        cerr << "Failed to write msg." << endl;
        return -1; 
    }         
    return 0;
}
```

## 测试文件Reader
```c++
#include "lm.helloworld.pb.h" 

void ListMsg(const lm::helloworld & msg) { 
    cout << msg.id() << endl; 
    cout << msg.str() << endl; 
}
  
int main(int argc, char* argv[]) { 
    lm::helloworld msg1; 

    { 
        fstream input("./log", ios::in | ios::binary); 
        if (!msg1.ParseFromIstream(&input)) { 
            cerr << "Failed to parse address book." << endl; 
            return -1; 
        }
    }

    ListMsg(msg1); 
}
```

# 5 高级应用话题
## 5.1 复杂的Message
### 嵌套的Message
```
message Person { 
 required string name = 1; 
 required int32 id = 2;        // Unique ID number for this person. 
 optional string email = 3; 
 
 enum PhoneType { 
   MOBILE = 0; 
   HOME = 1; 
   WORK = 2; 
 } 
 
 message PhoneNumber { 
   required string number = 1; 
   optional PhoneType type = 2 [default = HOME]; 
 } 
 repeated PhoneNumber phone = 4; 
}
```

### Import Message
```
import common.header; 
 
message youMsg{ 
 required common.info_header header = 1; 
 required string youPrivateData = 2; 
}
```

## 5.2 动态编译



# 参考资料
[Google Protocol Buffer 的使用和原理](https://www.ibm.com/developerworks/cn/linux/l-cn-gpb/index.html)
[protobuf序列化协议python教程](https://blog.csdn.net/luanpeng825485697/article/details/81029492)
