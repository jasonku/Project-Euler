'''
The decimal number, 585 = 1001001001_(2) (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

'''

from util import *

def palindromicString(str):
    for i in range(len(str)/2):
        if str[i] != str[len(str)-1-i]:
            return False
    return True



def main():

    sum = 0
    for i in range(1000000):
        if palindromicString(str(i)):
            if palindromicString(decimalToBinaryString(i)):
                sum += i
    return sum



if __name__ == "__main__":
    print main()
