#**************************Q0402.py**************************
# Author    : Yuichiro SUGA
# Email     : yuichiro.suga@centraliens-lille.org
# Created   : 2018-05-08 PM 06:35:00
# Modified  : 
# Mini quiz 2 
#************************************************************
import numpy as np

def getNormalVec(x, y):
    #if x  > 0 and y == 0:
    #    nx, ny = 0, 1
    #elif x == 0 and y > 0:
    #    nx, ny = -1, 0
    #elif x < 0 and y == 0:
    #    nx, ny = 0, -1
    #elif x == 0 and y < 0:
    #    nx, ny = 1, 0
    #elif x == 0 and y == 0:
    #    nx, ny = 0, 0
    #else:
    if x == 0:
        x = 1e-15
    if y == 0:
        y = 1e-15
    tan = x / y
    tan = - 1 / tan
    theta = np.arctan(tan)
    nx, ny = np.sin(theta), np.cos(theta)
    
    return (nx, ny)
