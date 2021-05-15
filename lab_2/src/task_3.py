from random import (
    randrange,
    sample
)
from builtins import pow


class GuessGame:
    """
    Класс игры в "угадайку"
    """

    def __init__(self,
                 p: int,
                 q: int
                 ):
        """
        Инициализация игры.
        @param p: простое число p
        @param q: простое число q
        @returns: объект игры
        """
        self.p = p
        self.q = q
        self.n = self.get_n(self.p, self.q)
        self.r = self.get_r(self.n)
        self.z = self.get_z(self.r, self.n)
        self.ring = Integers(self.n)
        self.roots = self.ring(self.z).sqrt(all=True)

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
    def get_r(n: int) -> int:
        """
        Получение числа r.
        @param n: произведение p и q
        @returns r: случайное число из интервала (0;n / 2)

        """
        return randrange(0, n // 2)

    @staticmethod
    def get_z(r: int, n: int) -> int:
        """
        Получение числа z.
        @param r: число r
        @param n: число n
        @returns z: r ^ 2 (mod n)

        """
        return pow(r, 2, n)

    def get_number(self) -> int:
        """
        Получение случайного корня из списка корней.
        @returns: корень
        """
        return sample(self.roots, 1)

    @staticmethod
    def is_answer(number: int, answer: int) -> bool:
        """
        Проверка ответа.
        @param number: догадка
        @param answer: загаданное число
        """
        return number == answer
