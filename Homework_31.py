# Ex_1

class Calculator:

    def __init__(self, num):
        if isinstance(num, int | float):
            self.__num = num
        else:
            raise ValueError("Input must be an integer or float")

    @property
    def number(self):
        return self.__num

    def __add__(self, other):
        return self.__num + other

    def __sub__(self, other):
        return self.__num - other

    def __mul__(self, other):
        return self.__num * other

    def __truediv__(self, other):
        return self.__num / other

    def __floordiv__(self, other):
        return self.__num // other

    def __mod__(self, other):
        return self.__num % other

    def __pow__(self, other):
        return self.__num ** other

    def __iadd__(self, other):
        self.__num += other
        return self.__num

    def __isub__(self, other):
        self.__num -= other
        return self.__num

    def __imul__(self, other):
        self.__num *= other
        return self.__num

    def __idiv__(self, other):
        self.__num /= other
        return self.__num

    def __ifloordiv__(self, other):
        self.__num //= other
        return self.__num

    def __imod__(self, other):
        self.__num %= other
        return self.__num

    def __ipow__(self, other):
        self.__num **= other
        return self.__num

    def __eq__(self, other):
        return self.__num == other

    def __gt__(self, other):
        return self.__num > other

    def __ge__(self, other):
        return self.__num >= other

    def __lt__(self, other):
        return self.__num < other

    def __le__(self, other):
        return self.__num <= other

    def __ne__(self, other):
        return self.__num != other

    def __str__(self):
        return str(self.__num)

    def __repr__(self):
        return f"Number({self.__num})"

