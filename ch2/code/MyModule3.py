#MyModule3.py
# Author: Yuichiro SUGA
# Created: 2018-04-17
# Modified: 2018-04-18
# Email: dmq0039@mail4.doshisha.ac.jp

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


#Quick sort
def getMax(a):
    if len(a) < 2:
        return a[0]
    
    pivot = a[0]
    ax = a[1:]
    #smaller = [x for x in ax if x <  pivot]
    larger  = [x for x in ax if x >= pivot]
    return getMax(larger)
