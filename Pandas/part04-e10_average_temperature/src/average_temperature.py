#!/usr/bin/env python3

# Exercise 4.10 (average temperature)
# Write function average_temperature that reads the weather data set and returns the average temperature in July.

# Print the result in the main function in the following form:

# Average temperature in July: xx.x

import pandas as pd

def average_temperature():

    df = pd.read_csv("src/kumpula-weather-2017.csv")

    july = df.loc[df.m == 7]

    avarage = july.loc[:, "Air temperature (degC)"].mean()

    return avarage

def main():

    temperature_july = average_temperature()

    print(f"Average temperature in July: {temperature_july}")

    return

if __name__ == "__main__":
    main()
