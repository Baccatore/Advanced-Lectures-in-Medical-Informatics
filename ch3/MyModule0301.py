#MyModule0301.py
# Author: Yuichiro SUGA
# Created: 2018-04-24
# Email: dmq0039@mail4.doshisha.ac.jp




def getAN(a, n1, n2):
    b = []
    if n1 + n2 > len(a):
        b = a[n1:]
    else :
        b = a[n1:n2+n1]
    return b
