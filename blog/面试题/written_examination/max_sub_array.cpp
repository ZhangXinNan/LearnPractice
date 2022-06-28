#include <climits>
#include <iostream>
using namespace std;

int get_max_sub_array(const int* arr, const int num) {
  int max_sum = INT_MIN;
  int sum = arr[0];
  for (int i = 1; i < num; i++) {
    if (sum < 0) 
      sum = arr[i];
    else
      sum += arr[i];
    if (sum > max_sum)
      max_sum = sum;
    
  }
  return max_sum;
}

int main() {
  int arr[] = {-1, 3, 2, -5, 3, -1, 7, -2, 1, 2, -10};
  int max_sum = get_max_sub_array(arr, sizeof(arr)/sizeof(arr[0]));
  cout << max_sum << endl;
  return 0;
}
