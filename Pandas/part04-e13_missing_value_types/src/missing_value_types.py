#!/usr/bin/env python3

# Exercise 4.13 (missing value types)
# Make function missing_value_types that returns the following DataFrame. Use the State column as the (row) index. The value types for the two other columns should be float and object, respectively. Replace the dashes with the appropriate missing value symbols.

# State	Year of independence	President
# United Kingdom	-	-
# Finland	1917	Niinistö
# USA	1776	Trump
# Sweden	1523	-
# Germany	-	Steinmeier
# Russia	1992	Putin


import pandas as pd
import numpy as np

def missing_value_types():

    df = pd.DataFrame([
        ["United Kingdom", np.nan, np.nan],
        ["Finland", 1917.0, "Niinistö"],
        ["USA", 1776.0, "Trump"],
        ["Sweden", 1523, np.nan],
        ["Germany", np.nan, "Steinmeier"],
        ["Russia", 1992.0, "Putin"]
    ], columns=["State", "Year of independence", "President"])

    df.set_index("State", inplace=True)

    return df
               
def main():

    print(missing_value_types())

    return

if __name__ == "__main__":
    main()
