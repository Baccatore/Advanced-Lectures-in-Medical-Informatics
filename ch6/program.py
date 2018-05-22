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
import matplotlib.pyplot as plt

import MyModule0701
import MyModule0702
import MyModule0703
import MyModule0708

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


    print("\nMyModule0703")
    li = MyModule0701.row2list(dF)
    s1 = li[1]; s2 = li[2]; s3 = li[3]
    df = pd.concat([s1,s2], axis=1);# print(type(df)); print(df)
    MyModule0703.addDF(df, s3) #print(df)
    #NOTE OK!

    print("Task 4")
    a = MyModule0701.row2list(dF)
    #n1 = int(input())
    #print(a[0],a[n1])
    #plt.scatter(a[0],a[n1])
    #plt.show()

    print("Task 5")
    print("Type 6 difital numbers")
    #li_show = map(int,input().split())
    #print(li_show)
    #for i, si in enumerate(li_show):
    #    plt.subplot(230+i+1)
    #    plt.scatter(a[0],a[si])
    #    #plt.xlabel("Time step"); plt.ylabel(a[si].name)
    #    #XXX Task 6
    #    plt.axvspan(1500,2500,facecolor='orange',alpha=0.3)
    #plt.show()

    print("Task 7")
    print("Type a digital number as n1")
   # d = int(input())
   # x = MyModule0702.extractRow(a[0],1500,1000)
   # y = MyModule0702.extractRow(a[d],1500,1000)
   # plt.scatter(x,y)
   # plt.show()

    print("MyModule0708")
    s1, s2 = a[1], a[2]
    s3, s4 = MyModule0702.extractRow(s1,1500,1000), MyModule0702.extractRow(s2,1500,1000)
    print(MyModule0708.getCorr(s3,s4))




