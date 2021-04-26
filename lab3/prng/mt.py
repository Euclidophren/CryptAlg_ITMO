class MT19937:
    def __init__(self, seed):
        self.n = 624
        self.x = [0] * self.n
        self.cnt = 0
        self.w = 32
        self.f = 1812433253
        self.m = 397
        self.r = 31
        self.a = 0x9908B0DF
        self.d = 0xFFFFFFFF
        self.b = 0x9D2C5680
        self.c = 0xEFC60000
        self.u = 11
        self.s = 7
        self.t = 15
        self.l = 18
        self.initialize(seed)

    def initialize(self, seed):
        self.x[0] = seed
        for i in range(1, self.n):
            self.x[i] = (self.f * (self.x[i - 1] ^ (self.x[i - 1] >> (self.w - 2))) + i) & ((1 << self.w) - 1)
        self.twist()

    def twist(self):
        for i in range(self.n):
            lower_mask = (1 << self.r) - 1
            upper_mask = (~lower_mask) & ((1 << self.w) - 1)
            tmp = (self.x[i] & upper_mask) + (self.x[(i + 1) % self.n] & lower_mask)
            tmp_a = tmp >> 1
            if tmp % 2:
                tmp_a = tmp_a ^ self.a
            self.x[i] = self.x[(i + self.m) % self.n] ^ tmp_a
        self.cnt = 0

    def temper(self):
        if self.cnt == self.n:
            self.twist()
        y = self.x[self.cnt]
        y = y ^ ((y >> self.u) & self.d)
        y = y ^ ((y << self.s) & self.b)
        y = y ^ ((y << self.t) & self.c)
        y = y ^ (y >> self.l)
        self.cnt += 1
        return y & ((1 << self.w) - 1)


def main():
    rng = MT19937(0)
    for i in range(10):
        print(rng.temper())


if __name__ == '__main__':
    main()
