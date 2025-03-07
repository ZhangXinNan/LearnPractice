
#include <iostream>


class Base{
    public:
    void Test(){ std::cout << __FUNCSIG__ << std::endl;}
}


class A: public Base{
    public:
    void Test(){ std::cout << __FUNCSIG__ << std::endl;}
}


class A: public Base{
    public:
    void Test(){ std::cout << __FUNCSIG__ << std::endl;}
}


void TestBase(Base& b){
    b.Test();
}


int main(){
    A a;
    B b;
    TestBase(a);
    TestBase(b);
}