

#include <iostream>
using namespace std;

const int row = 4;
const int col = 4;
int arr[row][col] = {
  {1, 2, 8, 9},
  {2, 4, 9, 12},
  {4, 7, 10, 13},
  {6, 8, 11, 15}
};
//const int** arr, const int row, const int col
bool find(int value) {
  int r_min = 0;
  int r_max = row;
  int c_min = 0;
  int c_max = col;
  return false;
}

int main() {
  cout << find(5) << endl;
  cout << find(7) << endl;

  return 0;
}
