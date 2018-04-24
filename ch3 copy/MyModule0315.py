#MyModule0315.py
# Author: Yuichiro SUGA
# Created: 2018-04-24
# Email: dmq0039@mail4.doshisha.ac.jp
import random

def printEven(a):
    for ax in a:
        if ax % 2 == 0:
            print(ax)


def printNumber(N):
    num = 0
    total = 0
    while total < N:
        num = random.randint(0,10)
        total += num
        print("+{:>2d}:".format(num), total)
    print("Total:", total)
