'''
n! means n x (n ? 1) x ... *3*2*1

Find the sum of the digits in the number 100!
'''

from util import *
def main():
    return sumDigits(factorial(100))
#    return sumDigits(93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000)
if __name__ == "__main__":
    print main()
