class BaseWELL:
    @staticmethod
    def mat_0_pos(t, v):
        return v ^ (v >> t)

    @staticmethod
    def mat_0_neg(t, v):
        return v ^ (v << (-t))

    @staticmethod
    def mat_1(v):
        return v

    @staticmethod
    def mat_3_pos(t, v):
        return v >> t

    @staticmethod
    def mat_3_neg(t, v):
        return v << (-t)

    @staticmethod
    def mat_4_neg(t, b, v):
        return v ^ ((v << (-t)) & b)

    @staticmethod
    def identity(v):
        return v