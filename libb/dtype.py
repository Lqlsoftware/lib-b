# Fraction with operators overload (add, sub, mul, div)
class Fraction():
    # construction
    def __init__(self, numerator, denominator:int=1, symbol:bool=None, precision:int=12):
        # decide symbol
        if symbol == None:
            self.symbol = (numerator >= 0 and denominator > 0) or (numerator < 0 and denominator < 0)
        else:
            self.symbol = symbol

        # parse float to fraction
        if type(numerator) == float:
            p = 10 ** precision
            n = int(abs(numerator) * p)
            d = int(abs(denominator) * p)
            nd_gcd = self.gcd(n, d)
            n = n // nd_gcd
            d = d // nd_gcd
            # we do not store more than 64 bits, transform to float
            if n.bit_length() > 32 and d.bit_length() > 32:
                self.numerator = abs(numerator) / abs(denominator)
                self.denominator = 1
            else:
                self.numerator = n
                self.denominator = d
        # parse int to fraction
        elif type(numerator) == int:
            n = abs(numerator)
            d = abs(denominator)
            nd_gcd = self.gcd(n, d)
            self.numerator = n // nd_gcd
            self.denominator = d // nd_gcd
        # unsupport type
        else:
            raise NotImplementedError

    # same symbol add
    def ssadd(self, other):
        n = self.numerator * other.denominator + other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Fraction(n, d, self.symbol)

    # same symbol sub
    def sssub(self, other):
        n = self.numerator * other.denominator - other.numerator * self.denominator
        d = self.denominator * other.denominator
        if n == 0:
            return Fraction(0)
        symbol = not(self.symbol ^ (n > 0))
        return Fraction(abs(n), d, symbol)

    def __float__(self):
        if self.symbol:
            return self.numerator / self.denominator
        else:
            return -self.numerator / self.denominator

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
        if type(self.numerator) == int:
            return "%s%d%s" % (("" if self.symbol else "-"), self.numerator, "" if self.denominator == 1 else ("/" + str(self.denominator)))
        else:
            return str(float(self))

    # overload abs()
    def __abs__(self):
        return Fraction(self.numerator, self.denominator)

    # Binary Operators
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
            return Fraction(n, d, symbol)
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
            return Fraction(n, d, symbol)
        else:
            return NotImplemented

    # overload op "//"
    def __floordiv__(self, other):
        return self.__truediv__(other)

    # overload op "%"
    def __mod__(self, other):
        return Fraction(float(self) % float(other))

    # overload op "**"
    def __pow__(self, other):
        return Fraction(float(self) ** other)

    # Comparison Operators
    # overload op "<"
    def __lt__(self, other):
        return not (self - other).symbol

    # overload op ">"
    def __gt__(self, other):
        return (self - other).symbol

    # overload op "<="
    def __le__(self, other):
        return (self == other) or (not (self - other).symbol)

    # overload op ">="
    def __ge__(self, other):
        return (self == other) or (self - other).symbol

    # overload op "=="
    def __eq__(self, other):
        return self.symbol == other.symbol and self.numerator == other.numerator and self.denominator == other.denominator

    # overload op "!="
    def __ne__(self, other):
        return self.symbol != other.symbol or self.numerator != other.numerator or self.denominator != other.denominator

    # Unary Operators
    # overload op "-"
    def __neg__(self):
        return Fraction(self.numerator, self.denominator, symbol=not self.symbol)

    # overload op "+"
    def __pos__(self):
        return Fraction(self.numerator, self.denominator)

