#!/usr/bin/env python3
#coding:utf8
#**************************MyModule0708**************************
# Author    : Yuichiro SUGA
# Email     : yuichiro.suga@centraliens-lille.org
# Created   : 2018-05-22 PM 10:54:35
# Modified  : 
# insert_comment_here
#************************************************************

import math
import itertools


def getCorr(s1,s2):
    x_sum = x_mean = x_abs = 0
    y_sum = y_mean = y_abs = 0
    denominator = numerator = 0; # x*y and |x|*|y|

    for xi, yi in zip(s1, s2):
        x_sum, y_sum = x_sum + xi, y_sum + yi

    x_mean, y_mean = x_sum/len(s1), y_sum/len(s2)

    for xi, yi in zip(s1,s2):
        numerator += (xi - x_mean) * (yi - y_mean)
        x_abs += (xi - x_mean)**2
        y_abs += (yi - y_mean)**2
    denominator = math.sqrt(x_abs) * math.sqrt(y_abs)

    return numerator/denominator
