from itertools import (
    islice,
    tee
)


def form_ngrams(text, n=2):
    ngrams = zip(*(islice(seq, index, None) for index, seq in enumerate(tee(text, n))))
    return ngrams


class Cipher(object):
    def encipher(self, string):
        return string

    def decipher(self, string):
        return string

    def a2i(self, ch):
        ch = ch.upper()
        arr = {
            'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,
            'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
            'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15,
            'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
            'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
        }
        return arr[ch]

    def i2a(self, i):
        i = i % 26
        arr = (
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        )
        return arr[i]


class Vigenere(Cipher):
    def __init__(self, key='fortification'):
        self.key = [k.upper() for k in key]

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


if __name__ == '__main__':
    test_string = 'rsxuvrdifbtkxvxgfhemhoeeei'
    key = 'TED'
    print(list(form_ngrams(test_string, 3)))
    cipher = Vigenere(key)
    decrypted = cipher.decipher(test_string)
    print(decrypted)
