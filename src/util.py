import math
import random
import heapq
from sets import *

def even(n):
    return n % 2 == 0

#def prime(n, k = 10):
#    for i in range(k):
#        if (random.randint(1, n-1)**(n-1)) % n != 1:
#            return False
#    return True
#

#

def prime(n):
    if n <= 1:
        return False
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True

def palindrome(n):
    return str(n) == str(n)[::-1]

def divisors(n):
    a = Set([])
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0 and i not in a:
            a.add(i)
            a.add(n/i)
    return a


pDivisors = {}

def properDivisors(n):
    if n in pDivisors:
        return pDivisors[n]
    if n == 0:
        return Set([0])
    d = divisors(n)
    d.remove(n)
    pDivisors[n] = d
    return d

def sumDigits(n):
    return sum(map(int, list(str(n))))

def factorial(n):
#    if n == 0 or n == 1: return 1

    return reduce(lambda x, y: x * y, range(1, n+1), 1)

alpha = {
'a':1,
'b':2,
'c':3,
'd':4,
'e':5,
'f':6,
'g':7,
'h':8,
'i':9,
'j':10,
'k':11,
'l':12,
'm':13,
'n':14,
'o':15,
'p':16,
'q':17,
'r':18,
's':19,
't':20,
'u':21,
'v':22,
'w':23,
'x':24,
'y':25,
'z':26
}

def valueOfWord(str):
    sum = 0
    for char in list(str):
        sum += alpha[char]
    return sum

def isPerfect(n):
    return sum(properDivisors(n)) == n

'''
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
'''
def isDeficient(n):
    return sum(properDivisors(n)) < n

sumOfProperDivisors = {}
abundants = {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False }
def isAbundant(n):


    if n in abundants:
        return abundants[n]

    if n in sumOfProperDivisors:
        s = sumOfProperDivisors[n]
    else:
        s = sum(properDivisors(n))
        sumOfProperDivisors[n] = s
    isAbundant = s > n
    abundants[n] = isAbundant
    return isAbundant



def decimalToBinaryString(n):
    bin = ''
    if n < 0:
        return bin
    if n == 0:
        return '0'
    while n > 0:
        bin = str(n % 2) + bin
        n = n >> 1
    return bin