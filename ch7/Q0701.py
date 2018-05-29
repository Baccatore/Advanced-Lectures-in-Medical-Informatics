#!/usr/bin/env python3
#coding:utf8
#**************************MyModule0701.py**************************
# Author    : Yuichiro SUGA
# Email     : yuichiro.suga@centraliens-lille.org
# Created   : 2018-05-22 PM 07:00:05
# Modified  : 
# insert_comment_here
#************************************************************

import pandas as pd


def row2list(dF):
    a =[]
    for series in dF:
        a.append(dF[series])
    return a
