#!/usr/bin/env python3

# Exercise 4.12 (cyclists)
# Write function cyclists that does the following.

# Load the Helsinki bicycle data set from the src folder (https://hri.fi/data/dataset/helsingin-pyorailijamaarat). The dataset contains the number of cyclists passing by measuring points per hour. The data is gathered over about four years, and there are 20 measuring points around Helsinki. The dataset contains some empty rows at the end. Get rid of these. Also, get rid of columns that contain only missing values. Return the cleaned dataset.

import pandas as pd

def cyclists():

    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(how='all')
    df = df.dropna(how='all', axis=1)

    return df


def main():

    print(cyclists())

    return
    
if __name__ == "__main__":
    main()
