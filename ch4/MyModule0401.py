#***********************MyModule0401.py**********************
# Author    : Yuichiro SUGA
# Email     : yuichiro.suga@centraliens-lille.org
# Created   : 2018-05-08 PM 07:42:54
# Modified  : Tue May  8 20:46:09 JST 2018
# My first module with pandas
#************************************************************

def mySaveExcel(df, s1, s2):
    df.to_excel(s1, sheet_name=s2)
