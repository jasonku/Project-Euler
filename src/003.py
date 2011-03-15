'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from util import *

def main():
    n = 600851475143
    h = []
    for i in range(2, int(math.ceil(math.sqrt(600851475143)))):
        if n <= 1:
            break
        if prime(i):
            while (n % i == 0):
                n /= i

            heapq.heappush(h, i)

    return h[-1]



#    n = 600851475143
#    i = 600851475142
#    while (i > 0):
#        if prime(i):
#            if n % i == 0:
#                return i
#        i -= 1


if __name__ == "__main__":
    print main()
