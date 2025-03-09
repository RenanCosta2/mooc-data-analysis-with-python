#!/usr/bin/env python3

# Exercise 4.9 (snow depth)
# Write function snow_depth that reads in the weather DataFrame from the src folder and returns the maximum amount of snow in the year 2017.

# Print the result in the main function in the following form:

# Max snow depth: xx.x

import pandas as pd

def snow_depth():

    df = pd.read_csv("src/kumpula-weather-2017.csv")

    snow = df.loc[:, "Snow depth (cm)"]

    return snow.max()

def main():

    max_snow = snow_depth()

    print(f"Max snow depth: {max_snow}")

    return

if __name__ == "__main__":
    main()
