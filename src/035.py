'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

from util import *

def rotate(str):
    return str[1:]+str[0]

def circularPrime(n):
    n = str(n)
    k = len(n)
    for i in range(k):
        if not prime(int(n)):
            return False
        else:
            n = rotate(n)
            
    return True

def main():
    count = 0
    for i in range(1000000):
        if circularPrime(i):
            count += 1

    return count




if __name__ == "__main__":
    print main()
