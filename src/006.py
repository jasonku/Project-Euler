'''
The sum of the squares of the first ten natural numbers is,
1^(2) + 2^(2) + ... + 10^(2) = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^(2) = 55^(2) = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 ? 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''

from util import *

def sumOfSquares(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum

def squareOfSums(n):
    return sum(range(1, n+1))**2

def main():
    n = 100
    return squareOfSums(n) - sumOfSquares(n)



if __name__ == "__main__":
    print main()
