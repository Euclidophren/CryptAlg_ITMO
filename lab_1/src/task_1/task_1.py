from CryptAlg_ITMO.lab_1.src.task_1.utils import *
from random import randrange

if __name__ == '__main__':
    nums = randrange(1000000000, 9999999999)
    print(nums)
    print(fermat_test(nums, 10))
    print(solovay_strassen(nums, 10))
