# -*t coding:utf-8 -*-
# Author: Yuichiro SUGA
# Email: dmq0039@mail4.doshisha.ac.jp
# Created: 2018/04/10
# Modified: 2018/04/10

import sys

#Definition of function
def fib(num):
    n1 = 0
    n2 = 1
    for i in range(num):
        n1, n2 = n2, n1+n2
    return n2

if __name__ == "__main__":
    #Print
    print('Hello, world!')
    print(sys.version)

    #List
    squares = [1, 4, 9, 16, 25]
    print(squares)
    print(type(squares))
    
    #Condition
    a = 10
    if a < 0:
        print("\na is smaller than 0")
    elif a == 0:
        print("\na is equal to 0")
    else:
        print("\na is bigger than 0")

    #Loop
    print("\nSquares from 1 to 5")
    for i in squares:
        print(i)
    print("\nIntegers from 1 to 5")
    for i in range(5):
        print(i)
    print("\nSquares from 1 to 5 by means of 'range'")
    for i in range(5):
        print(squares[i])

    #Call of original function
    print('\nFibonacci sequence')
    print(fib(10))

    #More list: Methods in list type
    a=[1,2,3,4]
    a.append(5)
    print(a)
    b=[]
    b.append('monkey')
    b.append('cat')
    b.append('dolphin')
    b.append('pecker')
    print(b)
    b.sort()
    print(b)
