from .base_well import BaseWELL


class WELL1024(BaseWELL):
    def __init__(self):
        self.w = 32
        self.r = 32
        self.m1 = 3
        self.m2 = 24
        self.m3 = 10
        self.fact = 2.32830643653869628906e-10
        self.state = [0] * self.r
        self.state_i = 0

    def wellrng_1024_a(self, init):
        self.state_i = 0
        for j in range(self.r):
            self.state[j] = init[j]

    def get_num(self):
        z0 = self.state[(self.state_i + 31) & 0x0000001f]
        z1 = self.state[self.state_i] ^ self.mat_0_pos(8, self.state[self.state_i + self.m1] & 0x0000001f)
        z2 = self.mat_0_neg(-19, self.state[(self.state_i + self.m2) & 0x0000001f]) ^ \
             self.mat_0_neg(-14, self.state[(self.state_i + self.m3) & 0x0000001f])
        self.state[self.state_i] = z1 ^ z2
        self.state[(self.state_i + 31) & 0x0000001f] = self.mat_0_neg(-11, z0) ^ \
                                                       self.mat_0_neg(-7, z1) ^ \
                                                       self.mat_0_neg(-13, z2)
        self.state_i = (self.state_i + 31) & 0x0000001f
        return self.state[self.state_i] * self.fact
