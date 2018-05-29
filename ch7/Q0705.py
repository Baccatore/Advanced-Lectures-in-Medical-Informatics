#!/usr/bin/env python3
#coding:utf8
#**************************Q0705.py**************************
# Author    : Yuichiro SUGA
# Email     : yuichiro.suga@centraliens-lille.org
# Created   : 2018-05-29 PM 06:43:54
# Modified  : 2018-05-29 PM 06:43:54
# 
#************************************************************

import pandas as pd

def getAve(s1):
    return s1.mean() 

def transMove(s1, d1):
    s2 = s1 - d1
    return s2

def transMoveAve (s1):
    ave = getAve(s1)
    s2 = transMove(s1, ave)
    return s2
