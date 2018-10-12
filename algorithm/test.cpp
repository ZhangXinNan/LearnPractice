
#include <iostream>
using namespace std;

int main(){
    int a[] = {5, 8, 13, 0, 1, 1876, 4};
    int size = sizeof(a) / sizeof(int);
    printf("%d\n", size);
    
    int *flag = new int[size+1];
    memset(flag, 0, (size+1)*sizeof(int));
    for(int i=0; i < size; i++){
        if(a[i] <= size){
            flag[a[i]] = 1;
        }
    }
    for(int i=0; i < size+1; i++){
        if(flag[i] == 0){
            std::cout << i << std::endl;
            break;
        }
    }
    delete []flag;
    return 0;
}