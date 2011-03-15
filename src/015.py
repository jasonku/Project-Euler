'''
Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.
How many routes are there through a 20x20 grid?
'''

from util import *

memoize = {}

def countPaths(N, M):
    if (N, M) in memoize:
        return memoize[(N, M)]
    if N == 1 or M == 1:
        return 1

    memoize[(N, M)] = countPaths(N-1, M) + countPaths(N, M-1)
    return memoize[(N, M)]

def main():
    # 20x20 grid means 21x21 spots
    return countPaths(21, 21)


if __name__ == "__main__":
    print main()
