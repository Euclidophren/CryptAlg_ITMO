from random import (
    randint, 
    randrange
)


def fermat_test(test_num, test_count):
    success_count = 0
    res = False
    for i in range(test_count):
        a = randint(2, test_num - 1)
        if pow(a, test_num - 1, test_num) == 1:
            success_count += 1
    if success_count == test_count:
        res = True
    return res


def legendre(a, p):
    if p < 2:
        raise ValueError('p must be greater than 2')
    if 0 < a < 2:
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


def solovay_strassen(test_num: int, test_count: int) -> bool:
    if 1 < test_num < 4:
        return True

    for _ in range(0, test_count):
        a = randrange(2, test_num-1)
        x = legendre(a, test_num)
        p = pow(a, (test_num - 1) / 2, test_num)
        if x == 0 or p != (x % test_num):
            return False
    return True
