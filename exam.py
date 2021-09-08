# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Programming in Python
# ## Exam: September 8, 2021
#
#
# You can solve the exercises below by using standard Python 3.9 libraries, NumPy, Matplotlib, Pandas, PyMC3.
# You can browse the documentation: [Python](https://docs.python.org/3.9/), [NumPy](https://numpy.org/doc/stable/user/index.html), [Matplotlib](https://matplotlib.org/3.3.1/contents.html), [Pandas](https://pandas.pydata.org/pandas-docs/version/1.2.5/), [PyMC3](https://docs.pymc.io/).
# You can also look at the [slides of the course](https://homes.di.unimi.it/monga/lucidi2021/pyqb00.pdf) or your code on [GitHub](https://github.com).
#
# **It is forbidden to communicate with others.** 
#

# %matplotlib inline
import numpy as np   # type: ignore
import pandas as pd  # type: ignore
import matplotlib.pyplot as plt # type: ignore
import pymc3 as pm   # type: ignore

# Your research team is studing a new protein, the *exambirulobin*, and they model its trend over time with the following differential equation.
#
# $  \frac{dy}{dt} = a + b\cdot y + c\cdot y^2 $
#
# Assume $a = 0.1$, $b = 0.02$, $c = 0.03$.
#
#

# ### Exercise 1 (max 4 points)
#
# Define a function to compute $\frac{dy}{dt}$ for any $y$. Make the function parametric in $a$, $b$, and $c$, but give them default values. 
#
#
# To get the full marks, you should declare correctly the type hints (the signature of the function) and add a doctest string.

pass

# ### Exercise 2 (max 5 points)
#
#
# Define a function to approximate the solution of the differential equation by leveraging on the [Euler method](https://en.wikipedia.org/wiki/Euler_method), considering that $\lim_{\Delta t \to 0} f(t + \Delta t) = f(t) + dt\cdot\frac{df}{dt}$. The function should take also the initial value for $t = 0$.
#
# To get the full marks, you should declare correctly the type hints (the signature of the function) and add a doctest string.

pass

# ### Exercise 3 (max 3 points)
#
# Plot the approximate solution, with a $\Delta t = .01$ on $0 \leq t < 15$. The value at $t = 0$ is $0.1$.

pass

# ### Exercise 4 (max 7 points)
#
# Experiments on *exambirulobin* samples resulted in the values stored in a file `values.csv` (first column). The corresponding measurements of the Calcium in the cell were recorded in the second column of `values.csv`

pass

# ### Exercise 5 (max 2 points)
#
# Define a Pandas DataFrame with the data in `values.csv` in two columns "exambirulobin" and "calcium".

pass

# ### Exercise 6 (max 3 points)
#
#
# Add to the dataframe two columns with the difference of the two measures in `values.csv` and the ratio of the difference and the *exambirulobin* value.

pass

# ### Exercise 7 (max 3 points)
#
# Make two adjacent plots: one with values of *exambirulobin* taken from `values.csv` and another with the histogram of the ratio computed in Exercise 6.

pass

# ### Exercise 8 (max 5 points)
#
# Consider this statistical model: the ratio computed in Exercise 6 is normally distributed, with an unknown mean, and a standard deviation of 1. Your *a priori* estimation of the mean is a normal distribution with mean 0 and standard deviation 1. Use PyMC to sample the posterior distributions after having seen the actual values of the ratio.  Plot the results.

pass


