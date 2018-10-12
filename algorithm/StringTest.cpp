
#include <iostream>
using namespace std;
//class String;
class String {
public:
  String(const char *str = NULL); // 普通构造函数 
  String(const String &other); // 拷贝构造函数 
  ~String(void); // 析构函数
  String& operate = (const String &other);// 赋值函数 
  void print() {
    std::cout << this->m_data << std::endl;
  }
private:
  char *m_data; // 用于保存字符串 
};

String::String(const char *str) // 普通构造函数 
{

}
String::String(const String &other)// 拷贝构造函数 
{

}
String::~String(void) // 析构函数 
{

}
String& String::operate = (const String &other)// 赋值函数 
{
    String tmp("");
    return tmp;
}


int main() {
    String s;
    String s1("123");
    String s2(s1);
    String s3 = s2;
    
    s.print();
    s1.print();
    s2.print();
    s3.print();
    return 0;
}