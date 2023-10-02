
#include <iostream>
#include <thread>

void hello() {
    std::cout << "Hello Concurrent World\n";
}

int main() {
    std::cout << "Hello World!--------" << std::endl;
    std::thread t(hello);
    // 主线程等待子线程。
    t.join();
    std::cout << "Hello World!========" << std::endl;
    return 0;
}

