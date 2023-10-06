
#include <iostream>


int main() {
    // int& i = 42;
    //error : non-const lvalue reference to type 'int' cannot bind to a temporary of type 'int'

    int&& i = 42;
    int j = 42;
    // int&& k = j;
    // error: rvalue reference to type 'int' cannot bind to lvalue of type 'int'
    return 0;
}