import numpy as np


class LFSR():
    def __init__(self, fpoly=[5, 2], initstate='ones', verbose=False):
        if isinstance(initstate, str):
            if initstate == 'ones':
                initstate = np.ones(np.max(fpoly))
            elif initstate == 'random':
                initstate = np.random.randint(0, 2, np.max(fpoly))
            else:
                raise Exception('Unknown intial state')
        if isinstance(initstate, list):
            initstate = np.array(initstate)

        self.initstate = initstate
        self.fpoly = fpoly
        self.state = initstate.astype(int)
        self.count = 0
        self.seq = np.array(-1)
        self.outbit = -1
        self.feedbackbit = -1
        self.verbose = verbose
        self.M = self.initstate.shape[0]
        self.expectedPeriod = 2 ** self.M - 1
        self.fpoly.sort(reverse=True)
        feed = ' '
        for i in range(len(self.fpoly)):
            feed = feed + 'x^' + str(self.fpoly[i]) + ' + '
        feed = feed + '1'
        self.feedpoly = feed

        self.check()

    def info(self):
        print('%d bit LFSR with feedback polynomial %s' % (self.M, self.feedpoly))
        print('Expected Period (if polynomial is primitive) = ', self.expectedPeriod)
        print('Current :')
        print(' State        : ', self.state)
        print(' Count        : ', self.count)
        print(' Output bit   : ', self.outbit)
        print(' feedback bit : ', self.feedbackbit)
        if self.count > 0 and self.count < 1000:
            print(' Output Sequence %s' % (''.join([str(int(x)) for x in self.seq])))

    def check(self):
        if np.max(self.fpoly) > self.initstate.shape[0] or np.min(self.fpoly) < 1 or len(self.fpoly) < 2:
            raise ValueError('Wrong feedback polynomial')
        if len(self.initstate.shape) > 1 and (self.initstate.shape[0] != 1 or self.initstate.shape[1] != 1):
            raise ValueError('Size of intial state vector should be one diamensional')
        else:
            self.initstate = np.squeeze(self.initstate)

    def set(self, fpoly, state='ones'):
        self.__init__(fpoly=fpoly, initstate=state)

    def reset(self):
        self.__init__(initstate=self.initstate, fpoly=self.fpoly)

    def changeFpoly(self, newfpoly, reset=False):
        newfpoly.sort(reverse=True)
        self.fpoly = newfpoly
        feed = ' '
        for i in range(len(self.fpoly)):
            feed = feed + 'x^' + str(self.fpoly[i]) + ' + '
        feed = feed + '1'
        self.feedpoly = feed

        self.check()
        if reset:
            self.reset()

    def next(self):
        b = np.logical_xor(self.state[self.fpoly[0] - 1], self.state[self.fpoly[1] - 1])
        if len(self.fpoly) > 2:
            for i in range(2, len(self.fpoly)):
                b = np.logical_xor(self.state[self.fpoly[i] - 1], b)

        self.state = np.roll(self.state, 1)
        self.state[0] = b * 1
        self.feedbackbit = b * 1
        if self.count == 0:
            self.seq = self.state[-1]
        else:
            self.seq = np.append(self.seq, self.state[-1])
        self.outbit = self.state[-1]
        self.count += 1
        if self.verbose:
            print('S: ', self.state)
        return self.state[-1]

    def runFullCycle(self):
        for i in range(self.expectedPeriod):
            self.next()
        return self.seq

    def runKCycle(self, k):
        tempseq = np.ones(k) * -1
        for i in range(k):
            tempseq[i] = self.next()

        return tempseq

    def _loadFpolyList(self):
        import os
        fname = 'primitive_polynomials_GF2_dict.txt'
        fname = os.path.join(os.path.dirname(__file__), fname)
        try:
            f = open(fname, "rb")
            lines = f.readlines()
            f.close()
            self.fpolyList = eval(lines[0].decode())
        except:
            raise Exception(
                "File named:'{}' Not Found!!! \n try again, after downloading file from github save it in lfsr "
                "directory".format(
                    fname))

    def get_fpolyList(self, m=None):
        self._loadFpolyList()
        if m is None:
            return self.fpolyList
        elif type(m) == int and 2 < m < 32:
            return self.fpolyList[m]
        else:
            print('Wrong input m. m should be int 1 < m < 32 or None')

    def get_Ifpoly(self, fpoly):
        if isinstance(fpoly, list) or (isinstance(fpoly, numpy.ndarray) and len(fpoly.shape) == 1):
            fpoly = list(fpoly)
            fpoly.sort(reverse=True)
            ifpoly = [fpoly[0]] + [fpoly[0] - ff for ff in fpoly[1:]]
            ifpoly.sort(reverse=True)
            return ifpoly
        else:
            print('Not a valid form of feedback polynomial')


if __name__ == '__main__':
    import doctest

    doctest.testmod()
