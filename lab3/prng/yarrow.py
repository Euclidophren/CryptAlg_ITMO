class BitBlock:
    def __init__(self,
                 full_bit_block,
                 left_bit_block,
                 right_bit_block,
                 permed_bit_block,
                 permed_left_bit_block,
                 permed_right_bit_block
                 ):
        self.full_bit_block = full_bit_block
        self.left_bit_block = left_bit_block
        self.right_bit_block = right_bit_block
        self.permed_bit_block = permed_bit_block
        self.permed_left_bit_block = permed_left_bit_block
        self.permed_right_bit_block = permed_right_bit_block

    def bit_block_split(self, permed):
        if permed:
            self.permed_left_bit_block = self.permed_bit_block.get(0, 28)
            self.permed_right_bit_block = self.full_bit_block.get(28, 56)
        else:
            self.left_bit_block = self.full_bit_block.get(0, 32)
            self.right_bit_block = self.full_bit_block.get(32, 64)

# TODO bitLock
# def bit_lock(self, permed):
#     if permed:


class Yarrow:
    @staticmethod
    def bytes_to_hex(bytes_string):
        return bytes_string.hex()
