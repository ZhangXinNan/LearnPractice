/*
作者：张欣
时间：2016-06-22 16：01
功能：将矩阵化为【简化阶梯形】
*/
#include <iostream>
#include <vector>
#include <iterator>
#include <sstream>
#include <algorithm>
using namespace std;

inline bool IsZero(double d) {
  if (d > -0.0001 && d < 0.0001) {
    return true;
  }
  return false;
}


void print_vv(const vector<vector<double> >& vv);
void print_v(const vector<string>& v);
size_t string_split(const string& str, vector<string> &sub);
void hang(vector<vector<double> >& m, const int r=0, const int c=0);
void simplify(vector<vector<double> >& m);
void sub(const vector<double>& v, vector<double>& u);
void sub(const vector<double>& v, vector<double>& u, double d);
void sub(const vector<double>& v, vector<double>& u) {
	for (size_t i = 0; i < v.size() && i < u.size(); i++) {
		u[i] -=v[i];
	}
}
void sub(const vector<double>& v, vector<double>& u, double d) {
	for (size_t i = 0; i < v.size() && i < u.size(); i++) {
		u[i] -= v[i] * d;
	}
}
int main(int argc, char* argv[]) {
  if (argc < 3) {
    cout << argc << endl;
    return 0;
  }
  vector<vector<double> > matrix;
  int row = atoi(argv[1]);
  int col = atoi(argv[2]);
  //string str = argv[3];
  cout << "row :" << row << ", col :" << col << endl;
  if (row < 2 || col < 2) {
    return 0;
  }
  matrix.resize(row);
  cout << "input matrix : （使用空格格开所有数）" << endl;
  for (size_t i = 0; i < row; i++) {
    matrix[i].resize(col, 0.0);
    for (size_t j = 0; j < col; j++) {
      //cout << "please input ("<<i<<","<<j<<")" << endl;
      string value;
      cin >> value;
      matrix[i][j] = atof(value.c_str());
    }
  }
  print_vv(matrix);
  hang(matrix);
  simplify(matrix);

  return 0;
}
//简化阶梯形
void simplify(vector<vector<double> >& m) {
	for (int y = m.size() - 1; y > 0; y--) {
		int flag_not_zero = -1;
		for (int x = 0; x < m[y].size() - 1; x++) {
			if ( IsZero(m[y][x] - 1.0) ) {
				flag_not_zero = x;
				break;
			}
		}
		if (flag_not_zero == -1) {
			continue;
		}
		for (int yy = y -1; yy >= 0; yy--) {
			if (!IsZero(m[yy][flag_not_zero])) {
				sub(m[y], m[yy], m[yy][flag_not_zero]);				
			}

		}
	}
	cout << "simplify -------" << endl;
	print_vv(m);
}

/*通过行初等变换，化为阶梯形*/
void hang(vector<vector<double> >& m, const int r, const int c) {
	if ( r < 0 || r > m.size() -1 || c < 0 || c > m[0].size() - 1) {
		return ;
	}
	int flag_not_zero = -1;
  for (size_t y = r; y < m.size(); y++) {
  	if (c >= m[y].size()) {
  		break;
  	}
  	if ( IsZero(m[y][c]) ) {
  	  continue;
  	} else if(flag_not_zero == -1) {
	  	flag_not_zero = y;  		
  	}

  	for (size_t x = c + 1; x < m[y].size(); x++) {
  	  m[y][x] /= m[y][c];
  	}
  	m[y][c] = 1.0;
  }
  cout << "r : " << r << ", c : " << c << endl;
  print_vv(m);

  if ( flag_not_zero == -1 ) {
  	hang(m, r, c + 1);
  	return ;
  } else if(flag_not_zero != r) {
  	m[r].swap(m[flag_not_zero]);
  }
  for (size_t y = r + 1; y < m.size(); y++) {
  	if ( !IsZero(m[y][c]) ) {
  		sub(m[r], m[y]);
  	}
  }
  cout << endl;
  print_vv(m);
  hang(m, r+1, c + 1);
}

size_t string_split(const string& str, vector<string> &sub) {
  return sub.size();
}

void print_v(const vector<string>& v) {
  for (size_t i = 0; i < v.size(); i++) {
    std::cout << "["<< i << "]" << v[i]<<endl;
  }
}

void print_vv(const vector<vector<double> >& vv) {
  for (size_t i = 0; i < vv.size(); i++) {
    for (size_t j = 0; j < vv[i].size(); j++) {
      printf("%6.3f ", vv[i][j]);
    }
    cout << ";" << endl;
  }
}
