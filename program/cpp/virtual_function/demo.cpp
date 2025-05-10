
#include <iostream>
#ifndef __FUNCSIG__
// #define __FUNCSIG__ __func__
#define __FUNCSIG__ __PRETTY_FUNCTION__
#endif


class Base{
    public:
    // 加了virtual 表示为抽象函数
    // virtual void Test(){ std::cout << __FUNCSIG__ << std::endl;}
    virtual void Test(int x){ std::cout << __FUNCSIG__ << " " << x << std::endl;}
};


class A: public Base{
    public:
    // void Test(){ std::cout << __FUNCSIG__ << std::endl;}
    void Test(int x){ std::cout << __FUNCSIG__ << " " << x << std::endl;}
};


class B: public Base{
    public:
    // void Test(){ std::cout << __FUNCSIG__ << std::endl;}
    void Test(int x){ std::cout << __FUNCSIG__ << " " << x << std::endl;}
};


void TestBase(Base& b){
    // b.Test();
    b.Test(99);
}

using Func = void(*)(void*, int);


int main(){
    A a;
    B b;
    TestBase(a);
    TestBase(b);
    // 不做任何操作的转换
    auto vptr = reinterpret_cast<void**>(&a);
    auto vtable = reinterpret_cast<void**>(*vptr);

    auto Test = reinterpret_cast<Func>(vtable[0]);
    Test(&a, 88);
}