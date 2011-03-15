'''
The following iterative sequence is defined for the set of positive integers:

n ? n/2 (n is even)
n ? 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 ? 40 ? 20 ? 10 ? 5 ? 16 ? 8 ? 4 ? 2 ? 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

'''

from util import *

memoize = {}

def lenOfChain(n):
    if n in memoize:
        return memoize[n]
    if n == 1:
        return 1
    if even(n):
        next = n / 2
    else:
        next = 3*n + 1
    memoize[n] = 1 + lenOfChain(next)
    return memoize[n]

def main():
    maxSoFar = 0
    maxStart = 1
    for n in range(1, 1000000):
        q = lenOfChain(n)
        if q > maxSoFar:
            maxSoFar = q
            maxStart = n
    return maxStart



if __name__ == "__main__":
    print main()
