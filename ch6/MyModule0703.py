#!/usr/bin/env python3
#coding:utf8
#**************************MyModule0703**************************
# Author    : Yuichiro SUGA
# Email     : yuichiro.suga@centraliens-lille.org
# Created   : 2018-05-22 PM 07:27:21
# Modified  : 
# insert_comment_here
#************************************************************


def addDF(df, s1):
    print(s1.name)
    df[s1.name] = s1[:]
