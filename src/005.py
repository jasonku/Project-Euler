'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

from util import *

def divisibleByAll(n, arr):
    for i in arr:
        if n % i != 0:
            return False

    return True


def main():
    i = 2520

    a = [19, 18, 17, 16, 15, 14, 13, 11]
    while True:
        if divisibleByAll(i, a):
            return i
        i += 20



if __name__ == "__main__":
    print main()
