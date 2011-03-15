'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

from util import *

def main():
    maxSoFar = 0
    for i in range(100, 999):
        for j in range(100, 999):
            p = i*j
            if p > maxSoFar and palindrome(p):
                maxSoFar = p
    return maxSoFar





#    n = 600851475143
#    i = 600851475142
#    while (i > 0):
#        if prime(i):
#            if n % i == 0:
#                return i
#        i -= 1


if __name__ == "__main__":
    print main()
