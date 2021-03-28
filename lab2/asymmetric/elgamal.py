import random
import sys


class PrivateKey(object):
    def __init__(self, p=None, g=None, x=None, i_numbits=0):
        self.p = p
        self.g = g
        self.x = x
        self.i_numbits = i_numbits


class PublicKey(object):
    def __init__(self, p=None, g=None, h=None, i_numbits=0):
        self.p = p
        self.g = g
        self.h = h
        self.i_numbits = i_numbits


def gcd(a, b):
    while b != 0:
        c = a % b
        a, b = b, c
    return a


def modexp(base, exp, modulus):
    return pow(base, exp, modulus)


def ss(num, i_confidence):
    for i in range(i_confidence):
        a = random.randint(1, num - 1)
        if gcd(a, num) > 1:
            return False
        if not jacobi(a, num) % num == modexp(a, (num - 1) // 2, num):
            return False
    return True


def jacobi(a, n):
    if a == 0:
        return 1 if n == 1 else 0
    elif a == -1:
        return -1 if n % 2 else 1
    elif a == 1:
        return 1
    elif a == 2:
        if n % 8 == 1 or n % 8 == 7:
            return 1
        elif n % 8 == 3 or n % 8 == 5:
            return -1
    elif a >= n:
        return jacobi(a % n, n)
    elif a % 2 == 0:
        return jacobi(2, n) * jacobi(a // 2, n)
    else:
        if a % 4 == 3 and n % 4 == 3:
            return -1 * jacobi(n, a)
        else:
            return jacobi(n, a)


def find_primitive_root(p):
    if p == 2:
        return 1
    p1 = 2
    p2 = (p - 1) // p1
    while 1:
        g = random.randint(2, p - 1)
        if not (modexp(g, (p - 1) // p1, p) == 1):
            if not modexp(g, (p - 1) // p2, p) == 1:
                return g


def find_prime(i_numbits, i_confidence):
    left_border, right_border = 2 ** (i_numbits - 2), 2 ** (i_numbits - 1)
    while 1:
        p = random.randint(left_border, right_border)
        while p % 2 == 0:
            p = random.randint(left_border, right_border)
        while not ss(p, i_confidence):
            p = random.randint(left_border, right_border)
            while p % 2 == 0:
                p = random.randint(left_border, right_border)
        p = p * 2 + 1
        if ss(p, i_confidence):
            return p


def encode(s_plaintext, i_numbits):
    byte_array = bytearray(s_plaintext, 'utf-16')
    z = []
    k = i_numbits // 8
    j = -1 * k
    for i in range(len(byte_array)):
        if i % k == 0:
            j += k
            z.append(0)
        z[j // k] += byte_array[i] * (2 ** (8 * (i % k)))
    return z


def decode(ai_plaintext, i_numbits):
    bytes_array = []
    k = i_numbits // 8
    for num in ai_plaintext:
        for i in range(k):
            temp = num
            for j in range(i + 1, k):
                temp = temp % (2 ** (8 * j))
            letter = temp // (2 ** (8 * i))
            bytes_array.append(letter)
            num = num - (letter * (2 ** (8 * i)))
    decoded_text = bytearray(b for b in bytes_array).decode('utf-16')
    return decoded_text


def generate_keys(i_numbits=256, i_confidence=32):
    p = find_prime(i_numbits, i_confidence)
    g = find_primitive_root(p)
    g = modexp(g, 2, p)
    x = random.randint(1, (p - 1) // 2)
    h = modexp(g, x, p)

    public_key = PublicKey(p, g, h, i_numbits)
    private_key = PrivateKey(p, g, x, i_numbits)

    return {'private_key': private_key, 'public_key': public_key}


def encrypt(key, s_plaintext):
    z = encode(s_plaintext, key.i_numbits)
    cipher_pairs = []
    for i in z:
        y = random.randint(0, key.p)
        c = modexp(key.g, y, key.p)
        d = (i * modexp(key.h, y, key.p)) % key.p
        cipher_pairs.append([c, d])

    encrypted_str = ""
    for pair in cipher_pairs:
        encrypted_str += str(pair[0]) + ' ' + str(pair[1]) + ' '

    return encrypted_str


def decrypt(key, cipher):
    plaintext = []

    cipher_array = cipher.split()
    if not len(cipher_array) % 2 == 0:
        return "Malformed Cipher Text"
    for i in range(0, len(cipher_array), 2):
        c = int(cipher_array[i])
        d = int(cipher_array[i + 1])

        s = modexp(c, key.x, key.p)
        plain = (d * modexp(s, key.p - 2, key.p)) % key.p
        plaintext.append(plain)

    decrypted_text = decode(plaintext, key.i_numbits)
    decrypted_text = "".join([ch for ch in decrypted_text if ch != '\x00'])

    return decrypted_text


def test():
    assert (sys.version_info >= (3, 4))
    keys = generate_keys()
    private_key = keys['private_key']
    public_key = keys['public_key']
    message = "My name is Ryan.  Here is some french text:  Maître Corbeau, sur un arbre perché." \
              "Now some Chinese: 鋈 晛桼桾 枲柊氠 藶藽 歾炂盵 犈犆犅 壾, 軹軦軵 寁崏庲 摮 蟼襛 蝩覤 蜭蜸覟 駽髾髽 忷扴汥 "
    cipher = encrypt(public_key, message)
    plain = decrypt(private_key, cipher)

    return message == plain
