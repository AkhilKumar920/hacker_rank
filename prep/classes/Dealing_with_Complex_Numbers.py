import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real_sum = self.real + other.real
        imag_sum = self.imaginary + other.imaginary
        return Complex(real_sum, imag_sum)

    def __sub__(self, other):
        real_diff = self.real - other.real
        imag_diff = self.imaginary - other.imaginary
        return Complex(real_diff, imag_diff)

    def __mul__(self, other):
        real_mul = (self.real * other.real) - (self.imaginary * other.imaginary)
        imag_mul = (self.real * other.imaginary) + (self.imaginary * other.real)
        return Complex(real_mul, imag_mul)

    def __truediv__(self, other):
        real_div = (self.real * other.real + self.imaginary * other.imaginary) / (other.real**2 + other.imaginary**2)
        imag_div = (self.imaginary * other.real - self.real * other.imaginary) / (other.real**2 + other.imaginary**2)
        return Complex(real_div, imag_div)

    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
