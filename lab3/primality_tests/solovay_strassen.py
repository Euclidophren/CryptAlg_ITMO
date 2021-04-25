import random


def legendre(a, p):
    if p < 2:
        raise ValueError('p must be greater than 2')
    if(a == 0) or (a == 1):
        return a
    if a % 2 == 0:
        re = legendre(a / 2, p)
        if p * p - 1 & 8 != 0:
            re *= -1
    else:
        re = legendre(p % a, a)
        if (a - 1) * (p - 1) & 4 != 0:
            re *= -1
    return re


def solovay_strassen(test_num, test_count):
    if test_num == 2 or test_num == 3:
        return True

    for _ in range(0, test_count):
        a = random.randrange(2, test_num-1)
        x = legendre(a, test_num)
        p = pow(a, (test_num - 1) / 2, test_num)
        if x == 0 or p != (x % test_num):
            return False
    return True
