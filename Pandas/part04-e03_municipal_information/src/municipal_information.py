#!/usr/bin/env python3

# Exercise 4.3 (municipal information)
# In the main function load a data set of municipal information from the src folder (originally from Statistics Finland). Use the function pd.read_csv, and note that the separator is a tabulator.

# Print the shape of the DataFrame (number of rows and columns) and the column names in the following format:

# Shape: r,c
# Columns:
# col1 
# col2
# ...
# Note, sometimes file ending tsv (tab separated values) is used instead of csv if the separator is a tab.

import pandas as pd

def main():

    df = pd.read_csv("src/municipal.tsv", sep="\t")

    print(f"Shape: {df.shape[0]},{df.shape[1]}")

    print("Columns:")
    for col in df.columns:
        print(col.strip())
    

    return


if __name__ == "__main__":
    main()
