
#include <stdio.h>
#include <string.h>
#include <math.h>

const int SIZE = 256;


char EXCESS_TABLE[256][9];
void init_excess_table() {
    printf("init_excess_table()-----------\n");
    memset(EXCESS_TABLE, '0', 256 * 9);
    for (int i = 0; i < 256; i++) {
        EXCESS_TABLE[i][8] = 0;
        int temp = i;
        for (int j = 7; j >= 0; j--) {
            if (temp == 0) {
                break;
            }
            if (temp % 2 == 1) {
                EXCESS_TABLE[i][j] = '1';
            }
            temp /= 2;
        }
        // printf("%d: %s\n", i, EXCESS_TABLE[i]);
    }
}


// 将十进制整数转成二进制，并保存到buff里。
void integer2str(const int value, char* buff, const int len) {
    printf("value: %d\n", value);
    int temp = value;
    int i = 0;
    char cache[SIZE];
    memset(cache, 0, SIZE);
    while (temp > 0) {
        if (temp % 2 == 0) {
            cache[i] = '0';
        } else {
            cache[i] = '1';
        }
        i++;
        temp /= 2;
    }
    printf("cache: %s\n", cache);
    for (int j = 0, k = i - 1; k >= 0 && j < len; j++, k--) {
        buff[j] = cache[k];
    }
    // for (int j = len - 1, k = 0; k < i && j >= 0; j--, k++) {
    //     buff[j] = cache[k];
    // }
    printf("buff: %s\n", buff);
}


void float2str(const float value, char* buff, const int len) {
    printf("value: %f\n", value);
    float temp = value;
    for (int i = 0; i < SIZE; i++) {
        double d = pow(0.5, i + 1);
        if (temp > d) {
            buff[i] = '1';
            temp -= d;
        } else {
            buff[i] = '0';
        }
        if (i > 100) {
            break;
        }
    }
}


void float_show(const float data, char* sd) {
    if (data >= 0.0f) {
        sd[0] = '0';
    } else {
        sd[0] = '1';
    }
    sd[1] = '-';
    printf("符号部分：%s\n", sd);

    printf("尾数部分的正则表达式\n");
    char integer_part[SIZE];
    char fractional_part[SIZE];
    memset(integer_part, 0, SIZE);
    memset(fractional_part, 0, SIZE);

    float value = fabsf(data);                  // 不再考虑符号，只看绝对值部分
    int value_int = (int)value;                 // 整数部分
    float value_float = value - value_int;      // 小数部分
    integer2str(value_int, integer_part, SIZE);
    printf("整数部分：%d, %s, %lu\n", value_int, integer_part, strlen(integer_part));
    float2str(value_float, fractional_part, SIZE);
    printf("浮点数部分：%f, %s\n", value_float, fractional_part);
    // return;

    int n = strlen(integer_part);
    char exp_part[9];
    memset(exp_part, '0', 8);
    exp_part[8] = 0;
    if (n > 1) {
        printf("整数部分位数：%d\n", n);
        integer2str(n - 1 + 127, exp_part, 9);
        memcpy(sd + 2, exp_part, 8);
        sd[10] = '-';
        memcpy(sd+11, integer_part + 1, n-1);
        memcpy(sd+11+n-1, fractional_part, 23 - n + 1);
    } else if (n == 1) {
        char* excess = "01111111";
        memcpy(sd + 2, excess, strlen(excess));
        sd[10] = '-';
        printf("指数部分：%s\n", excess);
        memcpy(sd + 11, fractional_part, 23);
        printf("尾数部分：%s\n", sd+11);
    } else {
        int i = 0;
        while(i < SIZE) {
            if (fractional_part[i] == '1') {
                break;
            }
            i++;
        }
        printf("%d, %d\n", i, 127-i-1);
        // integer2str(127 - i - 1, exp_part, 8);
        memcpy(exp_part, EXCESS_TABLE[127 - i - 1], 8);
        printf("%s\n", exp_part);
        memcpy(sd+2, exp_part, 8);
        sd[10] = '-';
        memcpy(sd + 11, fractional_part + i + 1, 23);
    }
    // printf("指数部分：\n");
    // printf("尾数部分：\n");

    printf("最终结果：%s\n", sd);
}



void float_bin_to_str(const float data, char* s) {
    unsigned long buff;
    int i;
    memcpy(&buff, &data, 4);

    for (i = 33; i >= 0; i--) {
        if (i == 1 || i == 10) {
            s[i] = '-';
        } else {
            if (buff % 2 == 1) {
                s[i] = '1';
            } else {
                s[i] = '0';
            }
            buff /= 2;
        }
    }
    s[34] = '\0';
}



int main() {
    init_excess_table();

    float data;
    // data = 0.75;
    scanf("%f", &data);
    printf("----------查看内存实际存储：\n");
    char str1[35];
    memset(str1, 0, 35);
    float_bin_to_str(data, str1);
    printf("%s\n", str1);

    printf("----------手动转换显示字符串：\n");
    char str2[SIZE];
    memset(str2, 0, SIZE);
    printf("%s %lu\n", str2, strlen(str2));
    float_show(data, str2);
    printf("%s\n", str2);



    printf("是否相等：%d\n", strcmp(str1, str2));
    printf("%s\n", str1);
    printf("%s\n", str2);
    return 0;
}