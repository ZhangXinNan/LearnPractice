
#include <thread>
#include <atomic>
#include <iostream>
#include <unistd.h>

// using namespace std;


std::atomic_flag lock = ATOMIC_FLAG_INIT;


void f(int n) {
    while (lock.test_and_set(std::memory_order_acquire)) {
        std::cout << "Waiting from thread " << n << std::endl;
    }
    std::cout << "Thread " << n << " starts working" << std::endl;
}


void g(int n) {
    std::cout << "Thread " << n << " is going to start." << std::endl;
    lock.clear();
    std::cout << "Thread " << n << " starts working" << std::endl;
}


int main() {
    lock.test_and_set();
    std::thread t1(f, 1);
    std::thread t2(g, 2);
    t1.join();
    usleep(100);
    t2.join();

    return 0;
}

