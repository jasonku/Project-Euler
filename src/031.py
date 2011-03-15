'''
In England the currency is made up of pound, $, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, $1 (100p) and $2 (200p).

It is possible to make $2 in the following way:

    1x$1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can $2 be made using any number of coins?

'''

from util import *

denoms = [1, 2, 5, 10, 20, 50, 100, 200]

# Let P(N) be number of ways to make A with the first N denominations
def P(A, N):
    if A < 0:
        return 0
    if A == 0:
        return 1
    if N < 0:
        return 0

    return P(A-denoms[N], N) + P(A, N-1)

def main():
    return P(200, 7)




if __name__ == "__main__":
    print main()
