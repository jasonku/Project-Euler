'''
Euler published the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 40^(2) + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n² ? 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, ?79 and 1601, is ?126479.

Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |?4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
'''

from util import *
from decimal import *

def lengthOfCycle(n):
    getcontext().prec = 99
    list(str(Decimal(1)/Decimal(n))[2:])


def main():
    maxLength = 0
    maxCycle = None
    for i in range(10,1000):
        d = lengthOfCycle(i)
        if d > maxLength:
            maxLength = d
            maxCycle = i

    return i


if __name__ == "__main__":
    print main()
