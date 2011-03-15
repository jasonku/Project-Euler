'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

from util import *
from sets import *
from time import *
#
#abundants = Set([])
#
#for i in range(12, 28123):
#    if isAbundant(i):
#        abundants.add(i)

#print abundants

#def generateAbundantsUpTo(n):
#    return abundants.intersection(Set(range(1, n+1)))

def canSumFromTwoAbundant(n):
#    d = generateAbundantsUpTo(n)
    for i in range(12, n/2+1):
#        print '--'
#        print d
#        print n
#        print i
        if isAbundant(i):
            if isAbundant(n-i):
                print str(i) + "+" + str(n-i) + "=" + str(n)
                return True
    return False


def main():
    sums = 0

#    last = 0
#    canSum = Set([])
#    for i in abundants:
#        for j in abundants:
#            s = i+j
#            if s < 28123:
#                if s not in canSum:
#                    canSum.add(i+j)
#            print len(canSum)
#    all = Set(range(24,28123))
#    cannotSum = all.difference(canSum)
#    return sum(list(cannotSum))

    last = 0
    for i in range(24, 28123):
#        t = clock()
        last += 1
#        if last > 1000:
#            print i
#            last = 0
        
        if not canSumFromTwoAbundant(i):
#            print i
#            last = 0
#            print i
#            sleep(1)
#            if last > 500:
#                print sum
#                last = 0
            sums += i
#        t2 = clock()
#        print "Iteration " + str(i) + " took " + str(t2 - t)
    return sums

if __name__ == "__main__":
    print main()
