#**********************MyModule0404.py************************
# Author    : Yuichiro SUGA
# Email     : yuichiro.suga@centraliens-lille.org
# Created   : 2018-05-08 PM 07:43:02
# Modified  : Tue May  8 20:47:05 JST 2018
# Last exercise of lecture #4 
#************************************************************
import pandas as pd

def mySaveExcel(df, s1, s2):
    df.to_excel(s1, sheet_name=s2)


def extract(s1, n1, n2):
    s = s1[n1:n2+1]
    return s


def MyMA(s1, n1):
    s = s1.rolling(window=n1).mean()
    s[0:n1-1] = 0 
    return s
