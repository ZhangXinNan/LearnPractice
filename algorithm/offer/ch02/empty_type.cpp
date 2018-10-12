#include <iostream>
using namespace std;

struct a{
};

class b{
  b(){}
  ~b(){}
};

class c{
  virtual ~c(){}
};

int main() {
  cout << sizeof(a) << endl;
  cout << sizeof(b) << endl;
  cout << sizeof(c) << endl;
  return 0;
}


/*
1
1
8
*/
