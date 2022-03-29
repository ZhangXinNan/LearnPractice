
# x > 1
def f(x, threshold=0.0000000001):
    left = 0
    right = x
    y = (left + right) / 2
    i = 0
    while abs(y * y - x) >= threshold:
        print("{}: y: {}, y * y: {}, y * y - x: {}".format(i, y, y * y, y * y - x))
        if y * y > x:
            right = y
            y = (left + y) / 2
        elif y * y < x:
            left = y
            y = (y + right) / 2
        i += 1
    return y


x = 2
y = f(x)
print('sqrt of {} is {}'.format(x, y))
print("y: {}, y * y: {}, y * y - x: {}".format(y, y * y, y * y - x))