from typing import Dict


class BaseCipher(object):
    def __init__(self,
                 alphabet: Dict,
                 p_box: list,
                 p_box_inv: list,
                 key: str = 'fortification',
                 ):
        self.alphabet = alphabet
        self.p_box = p_box
        self.p_box_inv = p_box_inv
        self.key = key

    def encipher(self, string):
        raise NotImplementedError

    def decipher(self, string):
        raise NotImplementedError

    def a2i(self, ch):
        ch = ch.upper()
        return self.alphabet[ch]

    def i2a(self, i):
        i = i % 26
        for k, v in self.alphabet.items():
            if v == i:
                return k


class Cipher(BaseCipher):
    def __init__(self,
                 alphabet: Dict,
                 p_box: list,
                 p_box_inv: list,
                 key: str = 'fortification'
                 ):
        super().__init__(alphabet, p_box, p_box_inv, key)

    def encipher(self, string):
        ret = ''
        for (i, c) in enumerate(string):
            i = i % len(self.key)
            ret += self.i2a(self.a2i(c) + self.a2i(self.key[i]))
        return ret

    def decipher(self, string):
        ret = ''
        for (i, c) in enumerate(string):
            i = i % len(self.key)
            ret += self.i2a(self.a2i(c) - self.a2i(self.key[i]))
        return ret

    def permute(self, state):
        res = 0
        for i in range(64):
            res += ((state >> i) & 0x01) << self.p_box[i]
        return res

    def inv_permute(self, state):
        res = 0
        for i in range(64):
            res += ((state >> i) & 0x01) << self.p_box_inv[i]
        return res

if __name__ == '__main__':
    # test_string = 'rsxuvrdifbtkxvxgfhemhoeeei'
    #
    # PBox = [0, 16, 32, 48, 1, 17, 33, 49, 2, 18, 34, 50, 3, 19, 35, 51,
    #         4, 20, 36, 52, 5, 21, 37, 53, 6, 22, 38, 54, 7, 23, 39, 55,
    #         8, 24, 40, 56, 9, 25, 41, 57, 10, 26, 42, 58, 11, 27, 43, 59,
    #         12, 28, 44, 60, 13, 29, 45, 61, 14, 30, 46, 62, 15, 31, 47, 63]
    # PBox_inv = [PBox.index(x) for x in range(64)]
    #

