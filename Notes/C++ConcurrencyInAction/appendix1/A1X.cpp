#include <iostream>

class X{
private:
    int* data;
public:
    X(): data(new int[1000000]){}
    ~X(){
        delete []data;
    }
    X(const X& other):data(new int[1000000]){
        std::copy(other.data, other.data + 1000000, data);
    }
    X(X&& other):data(other.data) {
        other.data = nullptr;
    }
    int* get() {
        return this->data;
    }
};


int main() {
    X x1;
    std::cout << x1.get() << std::endl;
    X x2 = std::move(x1);
    std::cout << x1.get() << ", " << x2.get() << std::endl;
    X x3 = static_cast<X&&>(x2);
    std::cout << x1.get() << ", " << x2.get() << ", " << x3.get() << std::endl;
    return 0;
}

