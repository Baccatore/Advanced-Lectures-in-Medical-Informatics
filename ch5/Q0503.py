#**************************Q0503.py**************************
# Author    : Yuichiro SUGA
# Email     : yuichiro.suga@centraliens-lille.org
# Created   : 2018-05-15 PM 06:27:58
# Modified  : Tue May 15 18:56:13 JST 2018
# Get tangent of 3rd order polynominal at point X
#************************************************************

import Q0501
import Q0502
import Q05

def getTan0(X,a,b,c,d):
    f  = Q0501.getF(X,a,b,c,d)
    df = Q0502.getDF(X,a,b,c)

    A = df
    B = -X*df + f
    if A == 0:
        return -99999
    else:
        return -B/A

if __name__ == "__main__":
    print("Q0501", Q0501.getF(2,1,2,3,4))
    print("Q0502", Q0502.getDF(2,1,2,3))
