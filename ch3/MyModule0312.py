#MyModule0312.py
# Author: Yuichiro SUGA
# Created: 2018-04-24
# Email: dmq0039@mail4.doshisha.ac.jp
import random

a = []
def getA(n):
    for x in range(n):
        a.append(random.random())
    return a

def printA():
    for ax in a:
        print(ax)


def getAverage(a):
    total = .0
    for ax in a:
        total += ax
    return total / len(a)


def getSquared(a):
    return [ax**2 for ax in a]


#Population variance
def getVariance(a):
    variance = .0
    average = getAverage(a)
    variance = getAverage(getSquared(a)) - average**2
    return variance

