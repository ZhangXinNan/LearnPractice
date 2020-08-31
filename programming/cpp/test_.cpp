

#include <iostream>
using namespace std;


int test(int a) {
    if ( a = 0xA | a > 12)
        if (011 & 10 == a) printf("%d\n", a);
        else printf("Right %d \n", a);
    else printf("Wrong %d\n", a);
    return 0;
}

int main() {
    // int a = 014;
    // int a = 0x14;
    test(014);
    test(0x14);

    return 0;
}