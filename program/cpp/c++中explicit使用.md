

# explicit 指定符
单词意思：
```
explicit : 明确的，清楚的
implicit : 含蓄的，暗示的。
```

1) 指定构造函数或转换函数 (C++11 起)为显式，即它不能用于**隐式转换**和**复制初始化**。
2) explicit 指定符可以与常量表达式一同使用。函数若且唯若该常量表达式求值为 true 才为显式。
(C++20 起)
explicit 指定符只可出现于构造函数或转换函数 (C++11 起)在其类定义内的 decl-specifier-seq 内。


# 示例
```c++
struct A
{
    A(int) { }      // 转换构造函数
    A(int, int) { } // 转换构造函数 (C++11)
    operator bool() const { return true; }
};
 
struct B
{
    explicit B(int) { }
    explicit B(int, int) { }
    explicit operator bool() const { return true; }
};
 
int main()
{
    A a1 = 1;      // OK ：复制初始化选择 A::A(int)
    A a2(2);       // OK ：直接初始化选择 A::A(int)
    A a3 {4, 5};   // OK ：直接列表初始化选择 A::A(int, int)
    A a4 = {4, 5}; // OK ：复制列表初始化选择 A::A(int, int)
    A a5 = (A)1;   // OK ：显式转型进行 static_cast
    if (a1) ;      // OK ：A::operator bool()
    bool na1 = a1; // OK ：复制初始化选择 A::operator bool()
    bool na2 = static_cast<bool>(a1); // OK ：static_cast 进行直接初始化
 
//  B b1 = 1;      // 错误：复制初始化不考虑 B::B(int)
    B b2(2);       // OK ：直接初始化选择 B::B(int)
    B b3 {4, 5};   // OK ：直接列表初始化选择 B::B(int, int)
//  B b4 = {4, 5}; // 错误：复制列表初始化不考虑 B::B(int,int)
    B b5 = (B)1;   // OK ：显式转型进行 static_cast
    if (b2) ;      // OK ：B::operator bool()
//  bool nb1 = b2; // 错误：复制初始化不考虑 B::operator bool()
    bool nb2 = static_cast<bool>(b2); // OK ：static_cast 进行直接初始化
}
```