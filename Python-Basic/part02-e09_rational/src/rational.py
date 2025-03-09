#!/usr/bin/env python3

# Exercise 2.9 (rational)
# Create a class Rational whose instances are rational numbers. A new rational number can be created with the call to the class. For example, the call r=Rational(1,4) creates a rational number “one quarter”. Make the instances support the following operations: + - * / < > == with their natural behaviour. Make the rationals also printable so that from the printout we can clearly see that they are rational numbers.

# For instance, given another rational number r2=Rational(2,3), the arithmetic operations r+r2, r-r2, r*r2, and r/r2 should return another instance of Rational representing the operation’s result. Boolean operations, like r>r2, should return a bool.

import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

class Rational(object):
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return (f'{self.num1}/{self.num2}')

    def __mul__(self, other):
        return Rational(self.num1 * other.num1, self.num2 * other.num2)
    
    def __truediv__(self, other):
        return Rational(self.num1 * other.num2, self.num2 * other.num1)

    def __add__(self, other):
        mmc = lcm(self.num2, other.num2)

        num1 = (mmc / self.num2) * self.num1
        num2 = (mmc / other.num2) * other.num1
        return Rational(num1 + num2, mmc)

    def __sub__(self, other):
        mmc = lcm(self.num2, other.num2)

        num1 = (mmc / self.num2) * self.num1
        num2 = (mmc / other.num2) * other.num1
        return Rational(num1 - num2, mmc)

    def __eq__(self, other):
        return self.num1/self.num2 == other.num1/self.num2

    def __lt__(self, other):
        return self.num1/self.num2 < other.num1/self.num2

    def __gt__(self, other):
        return self.num1/self.num2 > other.num1/self.num2
        
        

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
