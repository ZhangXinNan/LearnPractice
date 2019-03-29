
#include <cstdio>
//定义打印宏，并在打印信息前加入文件名、行号、函数名
 
//此宏展开后，类似于printf("123"),printf("456");
#define TRACE_CMH_1 (printf("%s(%d)-<%s>: ",__FILE__, __LINE__, __FUNCTION__), printf)
 
//此宏展开后，类似于printf("%d""%d", 1, 2);
#define TRACE_CMH_2(fmt,...) \
  printf("%s(%d)-<%s>: "##fmt, __FILE__, __LINE__, __FUNCTION__, ##__VA_ARGS__)
 
//注：由于第一个宏TRACE_CMH_1调用了两次printf，所以效率没有第二个宏高。
//如果编译器支持C99标准的话，可以用第二个宏。

//#include <iostream>
#include <string>
using  std::string;


int main(){
  string s = "hello";
  //cout << s << std::endl;
  printf(s.c_str());

  int count = 1;
  //打印当前行所在文件、行号、函数，以及其它信息。
	TRACE_CMH_1("SUB: [%d]\n", count++);
  // TRACE_CMH_2("BASE: [%d]\n", count++);

  return 0;
}

