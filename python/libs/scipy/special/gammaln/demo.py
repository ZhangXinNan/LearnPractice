
import math
def my_gammaln(n):
    s = 1
    for i in range(1, int(n)):
        s *= i
    return math.log(s)


if __name__ == '__main__':
    print([my_gammaln(x) for x in [1, 2, 3, 4, 5]])
    print([math.exp(my_gammaln(x)) for x in [1, 2, 3, 4, 5]])

    n = 10
    print(my_gammaln(n + 1))

    a, b = 2.0, 3.0
    print(my_gammaln(a) + my_gammaln(b) - my_gammaln(a + b))

    print(my_gammaln(171))

