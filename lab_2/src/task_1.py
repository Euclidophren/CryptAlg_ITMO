from random import randrange
import builtins


class Rabin:
    def __init__(self,
                 p: int,
                 q: int
                 ):
        self.p = p
        self.q = q
        self.n = self.get_n(self.p, self.q)
        self.m = randrange(1, self.n)

    @staticmethod
    def get_n(p: int, q: int) -> int:
        """
        Получение числа N.
        @param p: простое число p
        @param q: простое число q
        @returns: произведение p и q
        """
        return p * q

    @staticmethod
    def get_ms(c: int,
               p: int,
               q: int
               ):
        p_4, q_4 = (p + 1) // 4, (q + 1) // 4
        m1 = pow(c, p_4, p)
        m2 = -pow(c, p_4, p)
        m3 = pow(c, q_4, q)
        m4 = -pow(c, q_4, q)
        return m1, m2, m3, m4

    @staticmethod
    def get_pow(base: int,
                power: int
                ) -> int:
        """
        Возведение числа в степень по модулю
        :param base: основание
        :param power: степень
        :return: число
        """
        return base * pow(base, power - 2, power)

    def get_possible_messages(self,
                              a: int,
                              b: int,
                              c: int
                              ):
        m1, m2, m3, m4 = self.get_ms(c, self.p, self.q)
        message_1 = (a * m1 + b * m3) % self.n
        message_2 = (a * m1 + b * m4) % self.n
        message_3 = (a * m2 + b * m3) % self.n
        message_4 = (a * m2 + b * m4) % self.n
        return message_1, message_2, message_3, message_4

    @staticmethod
    def ascii_to_integer(text: str):
        """
        Перевод текста в число
        @param: text -- исходный текст
        @return: number -- числовое представление текста
        """
        number, r = 0, len(text)
        for i in range(r):
            number += (ord(text[i]) << (8 * i))
        return number

    @staticmethod
    def integer_to_ascii(num: int) -> str:
        """
        Перевод числа в текст.
        @param num: сумма символов в ASCII
        @returns res: бинарная строка.
        """
        res = builtins.str(builtins.bin(num)).replace('0b', '')
        counter = len(res) % 8
        for i in range(8 - counter):
            res = '0' + res
        return res
