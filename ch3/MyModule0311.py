#MyModule0311.py
# Author: Yuichiro SUGA
# Created: 2018-04-24
# Email: dmq0039@mail4.doshisha.ac.jp


import random

def getA(n):
    a = []
    for x in range(n):
        a.append(random.random())
    return a

def printA(a):
    for ax in a:
        print(ax)
