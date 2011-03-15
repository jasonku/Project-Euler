'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.


'''

from util import *

def sumOfFactorialOfDigits(n):
    return sum(map(factorial, map(int, list(str(n)))))

def main():
    i = 3
    sum = 0
    while True:
        s = sumOfFactorialOfDigits(i)
        if s == i:

            sum += i
            print sum
        i += 1

    return sum




if __name__ == "__main__":
    print main()
