#program.py
# Author: Yuichiro SUGA
# Created: 2018-04-17
# Email: dmq0039@mail4.doshisha.ac.jp
# This program is a demonstration of calling module from other code file in the same file.
import MyModule

MyModule.hello()
print('fib(10)=',MyModule.fib(10))
