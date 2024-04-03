
# "123456789" + "987654321" = "121932631112635269"

'''
def add_digit(x, nx, y, ny):
    # 0<=x<=9, 0<=y<=9
    # nx: x后有多少个零
    # ny: y后有多少个零
    z = x * y
    z0 = z % 10
    z1 = z // 10
    return z1, z0, nx + ny
'''


# print(add_digit(3, 2, 4, 2))
# print(add_digit(9, 2, 9, 2))

def add_result(c, z, n):
    y = c[-1 - n] + z
    if y < 10:
        c[-1-n] = y
        return c
    elif y >= 10:
        c[-1-n] = y % 10
        return add_result(c, y//10, n+1)


def add_big_number(a: str, b: str):
    a = [int(x) for x in a]
    b = [int(y) for y in b]
    c = [0] * (len(a) + len(b))

    for i in range(len(a)):
        for j in range(len(b)):
            a_i = a[-1-i]
            b_j = b[-1-j]
            print(i, j, f"数1：{a_i}, {i}, 数2：{b_j}, {j}")
            # z1, z0, n = add_digit(a[-1-i], i, b[-1-j], j)
            z = a_i * b_j
            z0, z1 = z % 10, z // 10
            z1 = z // 10
            print(z1, z0, i + j)
            if z1 > 0:
                c = add_result(c, z1, i + j +1)
                print(c)
            if z0 > 0:
                c = add_result(c, z0, i + j)
                print(c)
    return ''.join([str(x) for x in c]) 


a = "123456789"
b = "987654321"
result = "121932631112635269"

c = add_big_number(a, b)
print(c)

print(a, b)
print(result)

a, b = '999999', '999999'
c = add_big_number(a, b)
print(c)
print(int(a) * int(b))