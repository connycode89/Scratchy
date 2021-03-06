# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 14:26:03 2017

@author: cdonovan
"""

# Python 3.5
# Monte Carlo method of estimating pi

import random
import math
import pandas as pd

# radius = 1

def montecarlo_pi(num_iterations):
    num_circ = 0
    num_sq = 0
    for i in range(num_iterations):
        num_sq+=1
        p1, p2 = (random.random() for j in range(2))
        if (p1**2+p2**2)**0.5<=1:
            num_circ+=1

    pi_approx = 4*num_circ/num_sq

    # show results of simulation
    results = pd.DataFrame({'pi_approx':pi_approx, 'actual_pi':math.pi, 'percentage_error':(pi_approx-math.pi)*100/math.pi}, index=[0])
    return results

result_df = montecarlo_pi(100000)

# plot the absolute value of the error by various iteration sizes
import matplotlib.pyplot as plt
iter_sizes = range(1000, 1000000, 1000)
results2 = pd.DataFrame([(item, abs(montecarlo_pi(item)['percentage_error'][0])) for item in iter_sizes], columns=['num_iterations','abs_error'])

results2.plot(x='num_iterations', y='abs_error')
max1 = results2['abs_error'].max()+2
axes = plt.gca()
axes.set_ylim([0,max1])
