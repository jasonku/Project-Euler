'''
2^(15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^(1000)?
'''

from util import *

def main():
    return sumDigits(2**1000)


if __name__ == "__main__":
    print main()
