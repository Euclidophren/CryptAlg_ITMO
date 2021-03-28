import sys
from random import randrange
import struct
from math import sqrt
from argparse import ArgumentParser


def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--p', type=int, action='store', default=199, help='prime number p')
    parser.add_argument('--q', type=int, action='store', default=179, help='prime number q')
    return parser


def check_prime(number):
    ret = True
    for i in range(1, int(sqrt(number))):
        if number % i == 0:
            ret = False
    return ret


class RSA:
    def __init__(self, p, q):
        self._p = p
        self._q = q
        self._n = self._p * self._q
        self._phi = (self._p - 1) * (self._q - 1)
        self._e = self.get_e()
        self._d = self.get_d()

    def xgcd(self, a, b):
        x0, x1, y0, y1 = 0, 1, 1, 0
        while a != 0:
            q, b, a = b // a, a, b % a
            y0, y1 = y1, y0 - q * y1
            x0, x1 = x1, x0 - q * x1
        return b, x0, y0

    def mulinv(self, a, b):
        g, x, _ = self.xgcd(a, b)
        if g == 1:
            return x % b

    def get_e(self):
        while True:
            e = randrange(2, self._phi)
            modulus, x, _ = self.xgcd(self._e, self._phi)
            if modulus == 1:
                return e

    def get_d(self):
        d = self.mulinv(self._e, self._phi)
        return d

    def encrypt(self, filename_read, filename_write):
        with open(filename_read, "rb") as fr, open(filename_write, "w") as fw:
            data = fr.read()
            for item in data:
                new_item = pow(item, self._e, self._n)
                fw.write(str(new_item) + "\n")

    def decrypt(self, filename_read, filename_write):
        with open(filename_read, "r") as fr, open(filename_write, "wb") as fw:
            line = fr.readline()
            while line:
                num = int(line)
                byte = pow(num, self._d, self._n)
                fw.write(struct.pack('B', byte))
                line = fr.readline()


if __name__ == '__main__':
    filename = sys.argv[1]

    if len(sys.argv) == 2:
        p = 199
        q = 179
    else:
        p = int(sys.argv[2])
        q = int(sys.argv[3])
    rsa = RSA(p, q)
    with open(filename, 'rb') as file1:
        print("Encrypting...")
        rsa.encrypt(filename, filename.split(".")[0] + ".encoded")
        print("Decrypting...")
        rsa.decrypt(filename.split('.')[0] + ".encoded", filename.split('.')[0] + ".decoded")
