import random


def fermat_test(test_num, test_count):
    if test_num == 2:
        return True

    success_count = 0
    if test_count <= test_num / 10:
        test_count = test_num / 8
    for _ in range(0, test_count):
        a = random.randint(2, test_num - 1)
        if (a ** (test_num - 1)) % test_num == 1:
            success_count += 1
        else:
            return False
    if success_count == test_count:
        return True
