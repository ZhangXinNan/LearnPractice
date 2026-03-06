
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 普通引用
void DemoSort(vector<int>& v){
    sort(v.begin(), v.end());
}

// 右值引用
void DemoSort2(vector<int>&& v){
    sort(v.begin(), v.end());
}

int main(){
    vector<int> v{ 1, 3, 7, 2, 0, 8, 9, 6, 4, 5};
    // DemoSort(v);
    DemoSort2(std::move(v));
    for (auto item: v){
        cout << item << " ";
    }
    cout << endl;


    int a = 10;
    int& ra = a;
    int&& rra = std::move(a);
    cout << a << endl;
    ra = 11;
    cout << a << endl;
    rra = 12;
    cout << a << endl;
    return 0;
}