
#include <iostream>


void test1() {
    /************C++左值和右值**************/
    // 1) 可位于赋值号（=）左侧的表达式就是左值；反之，只能位于赋值号右侧的表达式就是右值。举个例子：
    int a = 5;
    // 5 = a; //错误，5 不能为左值
    // rvalue_ref.cpp:9:7: error: expression is not assignable

    // 其中，变量 a 就是一个左值，而字面量 5 就是一个右值。值得一提的是，C++ 中的左值也可以当做右值使用，例如：
    int b = 10; // b 是一个左值
    a = b; // a、b 都是左值，只不过将 b 可以当做右值使用
    // 2) 有名称的、可以获取到存储地址的表达式即为左值；反之则是右值。
}


void test2() {
    /************C++右值引用*****************/
    int num = 10;
    int &b = num; //正确
    // int &c = 10; //错误
    /* rvalue_ref.cpp:23:10: error: non-const lvalue reference to type 'int'
        cannot bind to a temporary of type 'int'
    */
}

void test3() {
    int num = 10;
    const int &b = num;
    const int &c = 10;
    /* 虽然 C++98/03 标准不支持为右值建立非常量左值引用，但允许使用常量左值引用操作右值。
    也就是说，常量左值引用既可以操作左值，也可以操作右值
    */
}


void test4() {
    /* 为此，C++11 标准新引入了另一种引用方式，称为右值引用，用 "&&" 表示。
    需要注意的，和声明左值引用一样，右值引用也必须立即进行初始化操作，且只能使用右值进行初始化，比如：
    */
    int num = 10;
    //int && a = num;  //右值引用不能初始化为左值
    int && a = 10;
    // 和常量左值引用不同的是，右值引用还可以对右值进行修改。例如：
    a = 100;
    std::cout << a << std::endl;

}


int main() {
    test1();
    test2();
    test3();
    test4();
    return 0;
}