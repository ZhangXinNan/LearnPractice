
#include <iostream>
#include <string>
using namespace std;


int main(){
    string str1 = "Hello";
    string str2 = str1;
    cout << str1 << "\t" << str2 << endl;
    str2[0] = 'a';
    cout << str1 << "\t" << str2 << endl;

    string str3 = "World";
    string str4 = std::move(str3);
    cout << str3 << "\t" << str4 << endl;
    str4[0] = 'a';
    cout << str3 << "\t" << str4 << endl;
    return 0;
}