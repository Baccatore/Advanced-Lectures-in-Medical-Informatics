#**********************MyModule0403.py***********************
# Author    : Yuichiro SUGA
# Email     : yuichiro.suga@centraliens-lille.org
# Created   : 2018-05-08 PM 07:43:00
# Modified  : Tue May  8 20:49:20 JST 2018
# Add myContact function to MyModule0402. This function conca-
# tenate two pandas serieses and return as one.
#************************************************************
import pandas as pd

def mySaveExcel(df, s1, s2):
    df.to_excel(s1, sheet_name=s2)


def extract(s1, n1, n2):
    s = s1[n1:n2+1]
    return s


def myConcat(s1, s2):
    s = pd.concat([s1, s2], axis=1)
    return s
