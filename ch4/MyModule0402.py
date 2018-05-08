#************************MyModule0402.py**********************
# Author    : Yuichiro SUGA
# Email     : yuichiro.suga@centraliens-lille.org
# Created   : 2018-05-08 PM 07:42:57
# Modified  : Tue May  8 20:45:39 JST 2018
# Add extract function to MyModule0401 
#************************************************************

def mySaveExcel(df, s1, s2):
    df.to_excel(s1, sheet_name=s2)


def extract(s1, n1, n2):
    s = s1[n1:n2+1]
    return s
