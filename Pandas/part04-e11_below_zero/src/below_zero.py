#!/usr/bin/env python3

# Exercise 4.11 (below zero)
# Write function below_zero that returns the number of days when the temperature was below zero.

# Print the result in the main function in the following form:

# Number of days below zero: xx

import pandas as pd

def below_zero():

    df = pd.read_csv("src/kumpula-weather-2017.csv")

    days_below_zero = df.loc[df.loc[:, "Air temperature (degC)"] < 0, "Air temperature (degC)"]

    return days_below_zero.count()

def main():

    number_days_below_0 = below_zero()

    print(f"Number of days below zero: {number_days_below_0}")

    return
    
if __name__ == "__main__":
    main()
