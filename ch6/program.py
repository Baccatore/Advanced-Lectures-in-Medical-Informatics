#!/usr/bin/env python3
#coding:utf8
#*********************program.py*****************************
# Author    : Yuichiro SUGA
# Email     : yuichiro.suga@centraliens-lille.org
# Created   : 2018-05-22 PM 06:25:27
# Modified  : 
# fNIRS data processing
#************************************************************

import pandas as pd

import MyModule0701
import MyModule0702


if __name__ == "__main__":
    book  = pd.ExcelFile("nirs.xlsx")
    dF = book.parse("01")

    print("MyModule0701")
    a = MyModule0701.row2list(dF)
    for ax in a:
        print(type(ax))
    #NOTE OK!

    print("MyModule0702")
    s1 = dF.Time
    print(type(s1),len(s1))
    s2 = MyModule0702.extractRow(s1, 5, 10)
    print(type(s2), len(s2))
    li = MyModule0701.row2list(dF)
    s1 = li[1]; print(type(s1))
    s2 = MyModule0702.extractRow(s1,1500,1000); print(type(s2))
    print(s2)


    print("MyModule0703")
