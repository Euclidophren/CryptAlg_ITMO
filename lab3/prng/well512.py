class WELL512:
    def __init__(self):
        self.w = 32
        self.r = 16
        self.p = 0
        self.m1 = 13
        self.m2 = 9
        self.m3 = 5
        self.fact = 2.32830643653869628906e-10
        self.state = [0] * self.r
        self.state_i = 0

    def wellrng512a(self, init):
        for j in range(self.r):
            self.state[j] = init[j]

    def get_num(self):
        z0 = self.state[(self.state_i + 15) & 0x0000000f]
        z1 = self.mat_0_neg(-16, self.state[self.state_i]) ^ \
             self.mat_0_neg(-15, self.state[(self.state_i + self.m1) & 0x0000000f])
        z2 = self.mat_0_pos(11, self.state[(self.state_i + self.m2) & 0x0000000f])
        self.state[self.state_i] = z1 ^ z2
        self.state[(self.state_i + 15) & 0x0000000f] = self.mat_0_neg(-2, z0) ^ \
                                                       self.mat_0_neg(-18, z1) ^ \
                                                       self.mat_3_neg(-28, z2) ^ \
                                                       self.mat_4_neg(-5, 0xda442d24, self.state[self.state_i])
        self.state_i = (self.state_i + 15) & 0x0000000f
        return self.state[self.state_i] * self.fact
