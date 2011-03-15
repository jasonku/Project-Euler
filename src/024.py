'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

from util import *
permutations = []
def permute(alist, level=0):
    index, copy, printing = level, list(alist), level+1 == len(alist)
    while 1:
        if printing:
            permutations.append(''.join(copy))
        else:
            permute(copy, 1+level);

        if index != 0:
            copy[index-1], copy[index] = copy[index], copy[index-1]

        index -= 1
        if index < 0:
            break


def main():
    str = "0123456789"
    permute(str)
    ints = map(int, permutations)
    ints.sort()
    return ints[999999]

if __name__ == "__main__":
    print main()
