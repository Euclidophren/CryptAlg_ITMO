from math import sqrt


def trial_division(number: int):
    res = True
    for i in range(int(sqrt(number))):
        if number % i:
            res = False
    return res
