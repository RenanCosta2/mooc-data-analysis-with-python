#!/usr/bin/env python3

# Exercise 5.5 (best record company)
# We use again the UK top 40 data set from the first week of 1964 in the src folder. Here we define "goodness" of a record company (Publisher) based on the sum of the weeks on chart (WoC) of its singles. Return a DataFrame of the singles by the best record company (a subset of rows of the original DataFrame). Do this with function best_record_company.

import pandas as pd

def best_record_company():

    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")

    records = df.groupby("Publisher")

    best_record = records["WoC"].sum().idxmax()

    return df.loc[df["Publisher"] == best_record]

def main():

    best_record = best_record_company()

    print(best_record)    

    return
    

if __name__ == "__main__":
    main()
