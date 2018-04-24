#MyModule0321.py
# Author: Yuichiro SUGA
# Created: 2018-04-24
# Email: dmq0039@mail4.doshisha.ac.jp

def getNumberEColi(k, x0, n1):
    x_i = x0 
    for n in range(n1):
        x_i = k*(1-x_i)*x_i
    return x_i
