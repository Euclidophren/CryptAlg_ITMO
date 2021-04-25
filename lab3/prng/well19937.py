from .base_well import BaseWELL


class WELL19937(BaseWELL):
    def __init__(self):
        self.w = 32
        self.r = 624
        self.p = 31
        self.m1 = 70
        self.m2 = 179
        self.m3 = 449
        self.mask_u = 0xffffffff >> (self.w - self.p)
        self.mask_l = ~self.mask_u
        self.state = [0] * self.r
        self.state_i = 0
        self.fact = 2.32830643653869628906e-10
        self.temper_b = 0xe46e1700
        self.temper_c = 0x9b868000
        self.tempering = False
        self.wellrng_19937a = None

    def wellrng19937a(self, init):
        self.state_i = 0
        self.wellrng_19937a = self.case_1()
        for j in range(self.r):
            self.state[j] = init[j]

    def get_num(self):
        if self.tempering:
            y = self.state[self.state_i] ^ ((self.state[self.state_i] << 7) & self.temper_b)
            y = y ^ ((y << 15) & self.temper_c)
            return y * self.fact
        else:
            return self.state[self.state_i] * self.fact

    def case_1(self):
        z0 = (self.state[self.state_i + self.r - 1] & self.mask_l) | \
             (self.state[self.state_i + self.r - 2] & self.mask_u)
        z1 = self.mat_0_neg(-25, self.state[self.state_i]) ^ \
             self.mat_0_pos(27, self.state[self.state_i + self.m1])
        z2 = self.mat_3_pos(9, self.state[self.state_i + self.m2]) ^ \
             self.mat_0_pos(1, self.state[self.state_i + self.m3])
        self.state[self.state_i] = z1 ^ z2
        self.state[self.state_i - 1 + self.r] = self.mat_1(z0) ^ \
                                                self.mat_0_neg(-21, z2) ^ \
                                                self.mat_0_pos(21, self.state[self.state_i])
        self.state_i = self.r - 1
        self.wellrng_19937a = self.case_3()
        return self.get_num()

    def case_2(self):
        z0 = (self.state[self.state_i - 1] & self.mask_l) | \
             (self.state[self.state_i + self.r - 2] & self.mask_u)
        z1 = self.mat_0_neg(-25, self.state[self.state_i]) ^ \
             self.mat_0_pos(27, self.state[self.state_i + self.m1])
        z2 = self.mat_3_pos(9, self.state[self.state_i + self.m2]) ^ \
             self.mat_0_pos(1, self.state[self.state_i + self.m3])
        self.state[self.state_i] = z1 ^ z2
        self.state[self.state_i - 1 + self.r] = self.mat_1(z0) ^ \
                                                self.mat_0_neg(-21, z2) ^ \
                                                self.mat_0_pos(21, self.state[self.state_i])
        self.state_i = 0
        self.wellrng_19937a = self.case_1()
        return self.get_num()

    def case_3(self):
        z0 = (self.state[self.state_i - 1] & self.mask_l) | \
             (self.state[self.state_i - 2] & self.mask_u)
        z1 = self.mat_0_neg(-25, self.state[self.state_i]) ^ \
             self.mat_0_pos(27, self.state[self.state_i + self.m1])
        z2 = self.mat_3_pos(9, self.state[self.state_i + self.m2]) ^ \
             self.mat_0_pos(1, self.state[self.state_i + self.m3])
        self.state[self.state_i] = z1 ^ z2
        self.state[self.state_i - 1 + self.r] = self.mat_1(z0) ^ \
                                                self.mat_0_neg(-21, z2) ^ \
                                                self.mat_0_pos(21, self.state[self.state_i])
        self.state_i -= 1
        if self.state_i + self.m1 < self.r:
            self.wellrng_19937a = self.case_5()
        return self.get_num()

    def case_4(self):
        z0 = (self.state[self.state_i - 1] & self.mask_l) | \
             (self.state[self.state_i + self.r - 2] & self.mask_u)
        z1 = self.mat_0_neg(-25, self.state[self.state_i]) ^ \
             self.mat_0_pos(27, self.state[self.state_i + self.m1])
        z2 = self.mat_3_pos(9, self.state[self.state_i + self.m2]) ^ \
             self.mat_0_pos(1, self.state[self.state_i + self.m3])
        self.state[self.state_i] = z1 ^ z2
        self.state[self.state_i - 1 + self.r] = self.mat_1(z0) ^ \
                                                self.mat_0_neg(-21, z2) ^ \
                                                self.mat_0_pos(21, self.state[self.state_i])
        self.state_i -= 1
        if self.state_i + self.m3 < self.r:
            self.wellrng_19937a = self.case_6()
        return self.get_num()

    def case_5(self):
        z0 = (self.state[self.state_i - 1] & self.mask_l) | \
             (self.state[self.state_i - 2] & self.mask_u)
        z1 = self.mat_0_neg(-25, self.state[self.state_i]) ^ \
             self.mat_0_pos(27, self.state[self.state_i + self.m1])
        z2 = self.mat_3_pos(9, self.state[self.state_i + self.m2]) ^ \
             self.mat_0_pos(1, self.state[self.state_i + self.m3 - self.r])
        self.state[self.state_i] = z1 ^ z2
        self.state[self.state_i - 1] = self.mat_1(z0) ^ \
                                       self.mat_0_neg(-21, z2) ^ \
                                       self.mat_0_pos(21, self.state[self.state_i])
        self.state_i -= 1
        if self.state_i + self.m2 < self.r:
            self.wellrng_19937a = self.case_4()
        return self.get_num()

    def case_6(self):
        z0 = (self.state[self.state_i - 1] & self.mask_l) | \
             (self.state[self.state_i - 2] & self.mask_u)
        z1 = self.mat_0_neg(-25, self.state[self.state_i]) ^ \
             self.mat_0_pos(27, self.state[self.state_i + self.m1])
        z2 = self.mat_3_pos(9, self.state[self.state_i + self.m2]) ^ \
             self.mat_0_pos(1, self.state[self.state_i + self.m3 - self.r])
        self.state[self.state_i] = z1 ^ z2
        self.state[self.state_i - 1] = self.mat_1(z0) ^ \
                                       self.mat_0_neg(-21, z2) ^ \
                                       self.mat_0_pos(21, self.state[self.state_i])
        self.state_i -= 1
        if self.state_i + self.m2 < self.r:
            self.wellrng_19937a = self.case_2()
        return self.get_num()
