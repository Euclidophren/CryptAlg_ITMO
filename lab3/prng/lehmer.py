import time

MODULUS = 2147483647     # DON'T CHANGE THIS VALUE
MULTIPLIER = 48271      # use 16807 for the "minimal standard"
CHECK = 399268537        # use 1043616065 for the "minimal standard"
STREAMS = 256             # # of streams, DON'T CHANGE THIS VALUE
A256 = 22925              # jump multiplier, DON'T CHANGE THIS VALUE
DEFAULT = 123456789      # initial seed, use 0 < DEFAULT < MODULUS
MAX_DRAWS = 8367782       # The number of calls to random separating each stream

Q_random = MODULUS / MULTIPLIER
R_random = MODULUS % MULTIPLIER
Q_seed = MODULUS / A256
R_seed = MODULUS % A256


class LehmerRNG(object):
    def __init__(self, initial_seed=DEFAULT, initial_stream=0):
        self.__stream = 0
        self.__seeds = [0] * STREAMS      # The current seeds of all the streams
        self.__num_draws = [0] * STREAMS  # For determining overflow
        self.stream = initial_stream      # The current stream
        self.seed = initial_seed
        self.plant_seeds(initial_seed)

    def __del__(self):
        for k in range(len(self.__num_draws)):
            if self.__num_draws[k] > MODULUS:
                print("Error: Stream %d completely cycled" % k)
            j = 1
            while self.__num_draws[k] > MAX_DRAWS:
                print("Error: Stream %d overlapped stream %d" % (k, (k+j) % STREAMS))
                self.__num_draws[k] -= MAX_DRAWS
                j += 1

    def random(self):
        self.__num_draws[self.stream] += 1 # Actual determination of cycling/overlapping is delayed for efficiency

        t = MULTIPLIER * (self.__seeds[self.stream] % Q_random) - R_random * (self.__seeds[self.stream] / Q_random)
        if t > 0:
            self.__seeds[self.stream] = t
        else:
            self.__seeds[self.stream] = t + MODULUS

        return float(self.__seeds[self.stream]) / MODULUS

    @property
    def seed(self):
        return self.__seeds[self.stream]

    @seed.setter
    def seed(self, new_seed):
        if new_seed > 0:
            new_seed %= MODULUS
        if new_seed < 0:
            new_seed = int(time.time()) % MODULUS
        if new_seed == 0:
            while new_seed <= 0 or new_seed >= MODULUS:
                new_seed = input("Enter a positive integer seed (9 digits or less) >> ")
        self.__seeds[self.stream] = new_seed

    def plant_seeds(self, x):
        s = self.stream                          # remember the current stream
        self.stream = 0                          # change to stream 0
        self.seed = x                            # set seed[0]
        self.stream = s                          # reset the current stream

        for j in range(1, STREAMS):
            x = A256 * (self.__seeds[j - 1] % Q_seed) - R_seed * (self.__seeds[j - 1] / Q_seed)
            if x > 0:
                self.__seeds[j] = x
            else:
                self.__seeds[j] = x + MODULUS

    @property
    def stream(self):
        return self.__stream

    @stream.setter
    def stream(self, index):
        self.__stream = index % STREAMS

    def test_random(self):
        self.stream = 0
        self.seed = 1
        for n in range(10000):
            self.random()
        x = self.seed

        self.stream = 1
        self.plant_seeds(1)
        y = self.seed

        if x == CHECK and y == A256:
            print("The implementation is correct")
        else:
            print("Error: the implementation is not correct")


if __name__ == '__main__':
    rng = LehmerRNG()
    rng.test_random()
