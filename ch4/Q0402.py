#**************************Q0402.py**************************
# Author    : Yuichiro SUGA
# Email     : yuichiro.suga@centraliens-lille.org
# Created   : 2018-05-08 PM 06:35:00
# Modified  : Tue May  8 21:10:19 JST 2018
# Mini quiz 2 
#************************************************************

import math

def getNormalVec(x, y):
    norm = x**2 + y**2
    norm = math.sqrt(norm)
    return (-y/norm, x/norm)
