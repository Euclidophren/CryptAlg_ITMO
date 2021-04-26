import numpy


class XORShift(object):
    def __init__(self, *args):
        self.seed(*args)

    def seed(self, *args):
        if len(args) > 4:
            raise ValueError('Algorithm accepts at maximum 4 integral seeds.')
        self.x = numpy.uint64(args[0] if len(args) > 0 else 0x123436789abcdef0)
        self.y = numpy.uint64(args[1] if len(args) > 1 else 0x456123abcdef0123)
        self.z = numpy.uint64(args[2] if len(args) > 2 else 0x9576503210fedcba)
        self.w = numpy.uint64(args[3] if len(args) > 3 else 0x6666666666666666)

    def next(self):
        t = self.x
        t ^= numpy.left_shift(t, numpy.uint64(11))
        t ^= numpy.right_shift(t, numpy.uint64(8))
        self.x = self.y
        self.y = self.z
        self.z = self.w
        self.w ^= numpy.right_shift(self.w, numpy.uint64(19))
        self.w ^= t
        return int(self.w)

    def rand_int(self, min, max):
        if min == max:
            return min
        else:
            return int(min + (self.next() % (max - min)))

    def rand_float(self, min=0, max=1):
        return float(min + (self.next() / float(18446744073709551615) * (max - min)))

    def rand_list(self, min_length, max_length, make_item):
        length = self.rand_int(
            min_length, max_length if max_length is not None else min_length
        )
        items = []
        for i in range(0, length):
            items.append(make_item())
        return items
