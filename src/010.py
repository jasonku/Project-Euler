'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from util import *

def main():
    sum = 2
    i = 3
    diff = 0
    while i < 2000000:
        if prime(i):
#            if diff > 1000:
#                print i
#                diff = 0
            sum += i
#        diff += 1
        i += 2
    return sum


if __name__ == "__main__":
    print main()
