#MyModule.py
# Author: Yuichiro SUGA
# Created: 2018-04-17
# Email: dmq0039@mail4.doshisha.ac.jp
def hello():
    print('hello world!')

def fib(n):
    if n==0 or n==1 :
        return 1
    else :
        return fib(n-2) + fib(n-1)

if __name__ == '__main__' :
    print('input n:'),
    i = int(input())
    print('fib(' + str(i) + ')=', fib(i))
