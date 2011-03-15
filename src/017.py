'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

from util import *

memoize = {
1:"one",
2:"two",
3:"three",
4:"four",
5:"five",
6:"six",
7:"seven",
8:"eight",
9:"nine",
10:"ten",
11:"eleven",
12:"twelve",
13:"thirteen",
14:"fourteen",
15:"fifteen",
16:"sixteen",
17:"seventeen",
18:"eighteen",
19:"nineteen",
20:"twenty",
30:"thirty",
40:"forty",
50:"fifty",
60:"sixty",
70:"seventy",
80:"eighty",
90:"ninety"
}

# Two digit nums
for i in range(21,100):
    if i not in memoize:
        tens = int(str(i)[0])*10
        ones = int(str(i)[1])
        memoize[i] = memoize[tens]+memoize[ones]

# Hundreds (100, 200, ...)
for i in range(1, 10):
    memoize[i*100] = memoize[i]+"hundred"

# Three digit nums
for i in range(100,1000):
    hun = int(str(i)[0])*100
    others = int(str(i)[1:3])
    if i not in memoize:
        memoize[i] = memoize[hun]+"and"+memoize[others]


def main():
    count = 0
    for i in range(1, 1000):
        count += len(str(memoize[i]))
    count += len(str("onethousand"))
    return count

if __name__ == "__main__":
    print main()
