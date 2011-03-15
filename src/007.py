'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6^(th) prime is 13.

What is the 10001^(st) prime number?
'''

from util import *


def main():
    count = 1
    i = 3
    last = 3
    while count != 10001:
        if prime(i):
            count += 1
            last = i
        i += 2
    return last


if __name__ == "__main__":
    print main()
