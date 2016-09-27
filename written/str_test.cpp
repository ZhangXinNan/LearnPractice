
/*
请实现一个函数，把字符串中的每一个函数替换成“%20”。例如输入“We are happy.”，则输出“We%20are%20happy.”。
*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char* str_replace(const char* str, const char* s1, const char* s2) {
    char* dest = 0;
    size_t len  = strlen(str);
    size_t len1 = strlen(s1);
    size_t len2 = strlen(s2);
    printf("%ld, %ld, %ld\n", len, len1, len2);

    int n = 0;
    for (int i = 0; i < len - len1 + 1; i++) {
        if (strncmp(str+i, s1, len1) == 0) {
            n++;
            i += len1 - 1;
        }
    }

    size_t len3 = len + n * (len2-len1) + 1;
    dest = new char[len3];
    memset(dest, 0, len3);//dest[len3 - 1] = 0;
    for (int i = 0, j = 0; i < len; ) {
        if ( i < len - len1 + 1 && strncmp(str + i, s1, len1) == 0) {
            strncpy(dest + j, s2, len2);
            j += len2;
            i += len1;
        } else {
            dest[j++] = str[i++];
        }
        printf("%s\n",dest);
    }

    return dest;
}

int main() {
    char* str = "We are happy.";
    char* s1 = "e ";
    char* s2 = "%20";
    char* dest = str_replace(str, s1, s2);
    printf("%s-->>%s\n", str, dest); 
    return 0;
}