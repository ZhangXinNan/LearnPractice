#pragma once

#include <stdio.h>
#include <io.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;


template <class T> inline const T& _max(const T& a, const T& b) {
	return a > b ? a : b;
}

template <class T> inline const T& _min(const T& a, const T& b) {
	return a < b ? a : b;
}

void SplitString(const std::string& s, std::vector<std::string>& v, const std::string& c);
int get_all_files(const string &in_dir, vector<string> &vec_file);

// 将HH:MM:SS:ms 转为毫秒的时间戳
long time2stamp(const string& t);
