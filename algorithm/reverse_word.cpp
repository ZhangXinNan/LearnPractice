

#include <iostream>
using namespace std;

void reverse(char* p, char* q) {
  while (q > p) {
    char c = *p;
    *p = *q;
    *q = c;
    p++;
    q--;
  }
}

void reverse_word(char* str, const int num) {
  reverse(str, str + num - 1);
  std::cout << str << endl;

  bool flag = false;
  int b, e;
  for (int i = 0; i < num; i++) {
    if (str[i] == ' ') {
      if (flag) {
        flag = false;
        reverse(str + b, str + e);
      } 
    } else {
      if (flag) {
	      e = i;
      } else {
        flag = true;
        b = e = i;  
      }
    }
  }
  if (e > b) {
    reverse(str + b, str + e);
  }
   
}


int main() {
  char str[] = "I'm have a good cat";
  cout << str << endl;
  cout << sizeof(str) << endl;
  reverse_word(str, sizeof(str)-1);
  cout << str << endl;
  return 0;
};
