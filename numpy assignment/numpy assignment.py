# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 00:12:00 2020

@author: reddymv
"""
import numpy as np
def moving_average(a, n=3):
    cum_sum = np.cumsum(a, dtype=float)
    cum_sum[n:] = cum_sum[n:]- cum_sum[:-n]
    return cum_sum[n-1:]/n

a=[3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
a1 = np.array(a)
np.array(moving_average(a1, n=3)).round(2)
