#**************************Q0401.py**************************
# Author    : Yuichiro SUGA
# Email     : yuichiro.suga@centraliens-lille.org
# Created   : 2018-05-08 PM 06:32:01
# Modified  : 
# Mini quiz
#************************************************************

def getMax(a, b, c):
    xmin, ymin = .0, .0
    xmin = - b / (2*a); ymin = (-b**2 + 4*a*c) / (4*a)
    return (xmin, ymin)
