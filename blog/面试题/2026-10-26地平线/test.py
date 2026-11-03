

'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。
'''

# twoSum([2,7,11,15], 9) == [0,1]


def f(arr, t):
    n = len(arr)
    if n < 2:
        print("数组长度小于2")
        return

    for i in range(n - 1):
        for j in range(i+1, n):
            if arr[i] + arr[j] == t:
                print(arr[i], arr[j], i, j)


def f2(arr, t):
    n = len(arr)
    if n < 2:
        print("数组长度小于2")
        return

    d = {}
    '''
    for j in range(n):
        if arr[j] in d:
            i = d[arr[j]]
            print(arr[i], arr[j], i, j)
        else:
            d[t - arr[j]] = j
    '''
    for j in range(n):
        if t - arr[j] in d:
            i = d[t - arr[j]]
            print(arr[i], arr[j], i, j)
        else:
            d[arr[j]] = j


a = [2, 2, 7, 11, 15]
t = 9
# f(a, t)
f2(a, t)



