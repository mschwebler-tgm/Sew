"""
Created on 23.10.2016

@author: Matthias Schwebler
"""

class Bruch(object):
    """
    This Class represents a fraction
    """

    def __init__(self, zaehler, nenner=1):
        """
        Constructor for fractions. Chekcs if nenner is zero.

        :param zaehler: numerator
        :param nenner: denominator
        """
        self.zaehler = zaehler
        self.nenner = nenner

        #Check for type
        if type(self.nenner) == float or type(self.zaehler) == float:
            raise TypeError

        #Check if nenner is 0
        if self.nenner == 0:
            raise ZeroDivisionError

    def __eq__(self, other):
        """
        Compares two fractions

        :param other: The fraction to be compared to
        :return: True if the two fractions ar equal - False if not
        """
        return float(self) == float(other)

    def __add__(self, other):
        """
        Adds a fraction to another one

        :param other: The fraction to be added
        :return: Sum of two fraction
        """
        if type(other) == int:
            return Bruch((self.zaehler + other * self.nenner), self.nenner)
        elif type(other) == Bruch:
            return Bruch((self.zaehler * other.nenner + other.zaehler * self.nenner), (self.nenner * other.nenner))
        else:
            raise TypeError

    def __iadd__(self, other):
        """
        Incremental addition

        :param other: The fraction to be added
        :return: Incremental sum of two fraction
        """
        return self.__add__(other)

    def __radd__(self, other):
        """
        Reverse addition

        :param other: The fraction to be added
        :return: Incremental sum of two fraction
        """
        return self.__add__(other)

    def __float__(self):
        """
        Returns the float-value of the fraction

        :return: The value of the fraction
        """
        return float(self.zaehler) / float(self.nenner)

    def __abs__(self):
        """
        Returns the absolute value of the fraction

        :return: The absolute value of the fraction
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __int__(self):
        """
        Returns the int-value of the fraction

        :return: The int-value of the fraction
        """
        return int(self.zaehler / self.nenner)

    def __invert__(self):
        """
        Swaps numerator with denominator

        :return: Inverted fraction
        """
        return Bruch(self.nenner, self.zaehler)

    def __neg__(self):
        """
        Negates the fraction

        :return: The negated fraction
        """
        return Bruch(self.zaehler, -self.nenner)

    def __pow__(self, power, modulo=None):
        """
        Takes the fraction to the given power

        :param power: exponent
        :param modulo:
        :return: The fraction to use
        """
        if type(power) == float:
            raise TypeError
        return Bruch(power ** self.zaehler, power ** self.nenner)

    @classmethod
    def __makeBruch(cls, value):
        """
        get fractions from ints

        :param value: Value to turn into a fraction
        :return: fraction
        """
        if type(value) == int:
            return Bruch(value)
        else:
            raise TypeError

    def __truediv__(self, other):
        """
        Divides the fraction with another one or an int

        :param other: The second fraction/int (divisor)
        :return: Result
        """
        if type(other) == int:
            if self == 0:
                raise ZeroDivisionError
            return float(self)*float(1/other)
        elif type(other) == Bruch:
            return float(self)*float(~other)
        else:
            raise TypeError

    def __itruediv__(self, other):
        """
        Incremental division

        :param other: The second fraction/int (divisor)
        :return: result
        """
        return self.__truediv__(other)

    def __rtruediv__(self, other):
        """
        Reverse division

        :param other: The second fraction/int (divisor)
        :return: result
        """
        return self.__truediv__(other)

    def __mul__(self, other):
        """
        Multiplies the fraction with another one

        :param other: The second fraction (factor)
        :return: result
        """
        if type(other) == int:
            return Bruch(self.zaehler*other, self.nenner)
        elif type(other) == Bruch:
            return Bruch(self.zaehler * other.zaehler, self.nenner * other.nenner)
        else:
            raise TypeError

    def __imul__(self, other):
        """
        Incremental multiplication

        :param other: The second fraction (factor)
        :return: result
        """
        return self.__mul__(other)

    def __rmul__(self, other):
        """
        Reverse multiplication

        :param other: The second fraction (factor)
        :return: result
        """
        return self.__mul__(other)

    def __sub__(self, other):
        """
        Subtracts a fraction

        :param other: The second fraction to be subtracted
        :return: result
        """
        if type(other) == int:
            return Bruch((self.zaehler - other * self.nenner), self.nenner)
        elif type(other) == Bruch:
            return Bruch((self.zaehler * other.nenner - other.zaehler * self.nenner), (self.nenner * other.nenner))
        else:
            raise TypeError

    def __isub__(self, other):
        """
        Incremental subtraction

        :param other: The second fraction to be subtracted
        :return: result
        """
        return self.__sub__(other)

    def __rsub__(self, other):
        """
        Reverse subtraction

        :param other: subtrahend
        :return: result
                """
        other = Bruch(other)
        return other.__sub__(self)

    def __str__(self):
        """
        Prints the fraction (readable)

        :return: "(Numerator/Denominator)"
        """
        if (self.zaehler < 0) and (self.nenner < 0):
            return "("+str(self.zaehler * -1) + "/" + str(self.nenner * -1) + ")"
        elif self.nenner == 1:
            return "("+str(self.zaehler) + ")"
        return "("+str(self.zaehler) + "/" + str(self.nenner) + ")"

    def __ge__(self, other):
        """
        Compares two fractions: >=

        :param other: The second fraction
        :return: True if float-value of self is greater or equal to float-value of *other*
        """
        return float(self) >= float(other)

    def __gt__(self, other):
        """
        Compares two fractions: >

        :param other: The second fraction
        :return: True if float-value of self is greater than float-value of *other*
        """
        return float(self) > float(other)

    def __le__(self, other):
        """
        Compares two fractions <=

        :param other: The second fraction
        :return: True if float-value of self is lesser or equal to float-value of *other*
        """
        return float(self) <= float(other)

    def __lt__(self, other):
        """
        Compares two fractions <

        :param other: The second fraction
        :return: True if float-value of self is less than float-value of *other*
        """
        return float(self) < float(other)

    def __iter__(self):
        """
        Iterates through the fraction

        :return: Iterator (numerator, denominator)
        """
        return (self.zaehler, self.nenner).__iter__()