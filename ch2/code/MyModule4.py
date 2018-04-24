#MyModule4.py
# Author: Yuichiro SUGA
# Created: 2018-04-17
# Email: dmq0039@mail4.doshisha.ac.jp
import random

def getATCG():
    gene = ['A', 'T', 'C', 'G']
    i = random.randrange(0, 3)
    return gene[i]

def printList(a):
    for ax in a:
        print(ax)
