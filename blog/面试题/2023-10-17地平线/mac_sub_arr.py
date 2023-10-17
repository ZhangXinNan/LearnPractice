

import random


def max_accu(arr):
    begin, end = 0, 1
    max_sum = arr[0]
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            tmp = 0
            for k in range(i, j):
                tmp += arr[k]
            if tmp > max_sum:
                max_sum = tmp
                begin, end = i, j
    return begin, end, max_sum


def max_accu2(arr):
    begin, end = 0, 1
    max_sum = arr[0]
    arr2 = [arr[0]]
    # 累加
    for i in range(1, len(arr)):
        arr2.append(arr[i] + arr2[i-1])
    print(arr2)

    for i in range(0, len(arr2)):
        for j in range(i + 1, len(arr2)):
            if i == 0:
                tmp = arr2[j]
            else:
                tmp = arr2[j] - arr2[i - 1]
            if tmp > max_sum:
                max_sum = tmp
                begin, end = i, j
    return begin, end, max_sum



random.seed(0)
a = [random.randint(-5, 5) for _ in range(10)]
print(a)

print(max_accu(a))
print(max_accu2(a))


