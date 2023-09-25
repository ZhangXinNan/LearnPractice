
#include <atomic>
#include <thread>
#include <iostream>
using namespace std;

// 原子数据类型
atomic_llong total {0};

void func(int) {
    for(long long i = 0; i < 100000000L; ++i) {
        total += i;
    }
}


int main() {
    thread t1(func, 0);
    thread t2(func, 0);
    
    t1.join();
    t2.join();
    cout << total << endl;
    return 0;
}