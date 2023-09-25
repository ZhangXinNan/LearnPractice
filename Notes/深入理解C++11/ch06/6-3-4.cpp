#include <thread>
#include <atomic>
#include <iostream>


std::atomic<int> a {0};
std::atomic<int> b {0};

int ValueSet(int) {
    int t = 1;
    a = t;
    b = 2;
    return 0;
}


int Observer(int) {
    std::cout << "(" << a << ", " << b << ")" << std::endl;
    return 0;
}


int main() {
    std::thread t1(ValueSet, 0);
    std::thread t2(Observer, 0);
    t1.join();
    t2.join();
    std::cout << "Got (" << a << ", " << b << ")" << std::endl;
    return 0;
}