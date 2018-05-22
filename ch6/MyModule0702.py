#!/usr/bin/env python3
#coding:utf8
#************************MyModule0702************************
# Author    : Yuichiro SUGA
# Email     : yuichiro.suga@centraliens-lille.org
# Created   : 2018-05-22 PM 07:11:44
# Modified  : 
# 
#************************************************************

import pandas as pd


def extractRow(s1, n1, n2):
    s2 = s1[n1:n1+n2]
    return s2
