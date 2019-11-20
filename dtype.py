# Fraction with operators overload (add, sub, mul, div)
class Fraction():
    # construction
    def __init__(self, numerator:int, denominator:int=1, symbol:bool=None):
        self.symbol = symbol
        self.numerator = numerator if numerator >= 0 else -numerator
        self.denominator = denominator if denominator >= 0 else denominator
        if symbol == None:
            self.symbol = (numerator >= 0 and denominator > 0) or (numerator < 0 and denominator < 0)

    # same symbol add
    def ssadd(self, other):
        n = self.numerator * other.denominator + other.numerator * self.denominator
        d = self.denominator * other.denominator
        nd_gcd = self.gcd(n, d)
        return Fraction(n // nd_gcd, d // nd_gcd, self.symbol)

    # same symbol sub
    def sssub(self, other):
        n = self.numerator * other.denominator - other.numerator * self.denominator
        d = self.denominator * other.denominator
        if n == 0:
            return Fraction(0)
        symbol = not(self.symbol ^ (n > 0))
        n = abs(n)
        nd_gcd = self.gcd(n, d)
        return Fraction(n // nd_gcd, d // nd_gcd, symbol)

    # use gcd to simplfiy fraction
    @staticmethod
    def gcd(a, b):
        if a < b:
            a, b = b, a
        while (b != 0):
            a, b = b, a % b
        return a

    # overload print()
    def __str__(self):
        return "%s%d%s" % (("" if self.symbol else "-"), self.numerator, "" if self.denominator == 1 else ("/" + str(self.denominator)))

    # overload abs()
    def __abs__(self):
        return Fraction(self.numerator, self.denominator)

    # overload op "+"
    def __add__(self, other):
        if isinstance(other, Fraction):
            # diff symbol
            if self.symbol != other.symbol:
                return self.sssub(other)
            # calculate add
            return self.ssadd(other)
        else:
            return NotImplemented

    # overload op "-"
    def __sub__(self, other):
        if isinstance(other, Fraction):
            # diff symbol
            if self.symbol != other.symbol:
                return self.ssadd(other)
            # calculate sub
            return self.sssub(other)
        else:
            return NotImplemented

    # overload op "*"
    def __mul__(self, other):
        if isinstance(other, Fraction):
            symbol = not(self.symbol ^ other.symbol)
            n = self.numerator * other.numerator
            d = self.denominator * other.denominator
            if n == 0:
                return Fraction(0)
            nd_gcd = self.gcd(n, d)
            return Fraction(n // nd_gcd, d // nd_gcd, symbol)
        else:
            return NotImplemented

    # overload op "/"
    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ZeroDivisionError
            symbol = not(self.symbol ^ other.symbol)
            n = self.numerator * other.denominator
            d = self.denominator * other.numerator
            if n == 0:
                return Fraction(0)
            nd_gcd = self.gcd(n, d)
            return Fraction(n // nd_gcd, d // nd_gcd, symbol)
        else:
            return NotImplemented

    # overload op "=="
    def __eq__(self, other):
        return self.symbol == other.symbol and self.numerator == other.numerator and self.denominator == other.denominator

    # overload op "<="
    def __le__(self, other):
        return (self == other) or (not (self - other).symbol)

    # overload op "<"
    def __lt__(self, other):
        return not (self - other).symbol

    # overload op ">="
    def __ge__(self, other):
        return (self == other) or (self - other).symbol

    # overload op ">"
    def __gt__(self, other):
        return (self - other).symbol

    # TODO overload op "**"