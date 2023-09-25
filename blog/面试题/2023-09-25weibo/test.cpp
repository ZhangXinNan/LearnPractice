

/*
最长回文子串：如果一个字符串正着读和反着读是一样的，那它就是回文串
给你一个字符串 s，找到 s 中最长的回文子串
*/
#include <iostream>
using namespace  std;


int check(const string& s, const size_t i, string &result) {
    int len = 1;
    string tmp = string("") + s[i];
    int begin = i;

    int m = i - 1, n = i + 1;
    while (n < s.size() && m >= 0 && s[m] == s[n]) {
        len += 2;   // 记录回文长度
        begin = m;  // 记录起始位置
        m -= 1;
        n += 1;
    }
    std::cout << begin << "," << len << std::endl;
    result = s.substr(begin, len);
    return len;
}

int check2(const string& s, const size_t i, string &result) {
    int len = 0;
    string tmp = "";
    int begin = i;

    int m = i, n = i + 1;
    while (n < s.size() && m >= 0 && s[m] == s[n]) {
        len += 2;
        begin = m;
        m -= 1;
        n += 1;
    }
    std::cout << begin << "," << len << std::endl;
    result = s.substr(begin, len);
    return len;
}

class Solution {
public:
    string longestPalindrome(const string& s) {
        string max_str = "";
        string tmp_str = "";
        size_t max_len = 0;
        size_t tmp_len = 0;
        for (size_t i = 0; i < s.size(); i++) {
            tmp_len = check(s, i, tmp_str);
            if (tmp_len > max_len) {
                max_len = tmp_len;
                max_str = tmp_str;
            }
            tmp_len = check2(s, i, tmp_str);
            if (tmp_len > max_len) {
                max_len = tmp_len;
                max_str = tmp_str;
            }
        }
        return max_str;
    }
};


int main() {
    std::string s1 = "123abcba345";
    std::string s2 = "123abccba345";
    Solution solution;
    std::cout << s1 << std::endl;
    std::string r1 = solution.longestPalindrome(s1);
    std::cout << r1 << std::endl;
    std::cout << s2 << std::endl;
    std::string r2 = solution.longestPalindrome(s2);
    std::cout << r2 << std::endl;
    
    return 0;
}