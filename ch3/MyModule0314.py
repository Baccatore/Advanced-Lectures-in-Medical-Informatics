#MyModule0314.py
# Author: Yuichiro SUGA
# Created: 2018-04-24
# Email: dmq0039@mail4.doshisha.ac.jp

import math
import itertools

def getNorm(a):
    norm = .0
    for ax in a:
        norm += ax**2
    norm = math.sqrt(norm)
    return norm

def getProduct(a, b):
    inner_product = .0
    for ax, bx in zip(a,b):
        inner_product += ax * bx
    return inner_product

