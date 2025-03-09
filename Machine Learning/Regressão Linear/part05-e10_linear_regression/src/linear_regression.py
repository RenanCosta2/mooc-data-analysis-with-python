#!/usr/bin/env python3

# Exercise 5.10 (linear regression)
# This exercise can give two points at maximum!

# Part 1.

# Write a function fit_line that gets one dimensional arrays x and y as parameters. The function should return the tuple (slope, intercept) of the fitted line. Write a main program that tests the fit_line function with some example arrays. The main function should produce output in the following form:


# Slope: 1.0
# Intercept: 1.16666666667
# Part 2.

# Modify your main function to plot the fitted line using matplotlib, in addition to the textual output. Plot also the original data points.

# %%
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# %%
def fit_line(x, y):

    reg = LinearRegression()

    reg.fit(x[:, np.newaxis], y)

    a, b = reg.intercept_, reg.coef_[0]

    return b, a
    
    # %%
def main():

    np.random.seed(0)
    n = 20
    ages = np.linspace(0, 10, n) 
    heights = 2 * ages + 1 + np.random.randn(n)
    
    reg = LinearRegression()
    reg.fit(ages[:, np.newaxis], heights)

    predict = reg.predict(ages[:, np.newaxis])

    # %%
    a, b = fit_line(ages, heights)

    print(f"Slope: {a:.1f}")
    print(f"Intercept: {b:.10f}")

    # %%
    plt.plot(ages, heights, 'o')
    plt.plot(ages, predict, '-')
    plt.grid(True)
    plt.xlabel("Ages")
    plt.ylabel("Heights")
    plt.show()
    

# %%
if __name__ == "__main__":
    main()
