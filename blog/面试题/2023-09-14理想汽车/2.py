
def merge(m: list, n: list):
    result = []
    i, j = 0, 0
    while True:
        if i < len(m) and j < len(n):
            if m[i] <= n[j]:
                result.append(m[i])
                i += 1
            else:
                result.append(n[j])
                j += 1
        elif i >= len(m) and j < len(n):
            result.append(n[j])
            j += 1
        elif i < len(m) and j >= len(n):
            result.append(m[i])
            i += 1
        else:
            break
    return result


m = [1,3,5,7]
n = [2,4,6]
result = merge(m, n)
print(result)
