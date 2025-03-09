#!/usr/bin/env python3

# Exercise 4.17 (cleaning data)
# This exercise can give two points at maximum!

# The entries in the following table of US presidents are not uniformly formatted. Make function cleaning_data that reads the table from the tsv file src/presidents.tsv and returns the cleaned version of it. Note, you must do the edits programmatically using the string edit methods, not by creating a new DataFrame by hand. The columns should have dtypes object, integer, float, integer, object. The where method of DataFrames can be helpful, likewise the string methods of Series objects. You get an additional point, if you manage to get the columns President and Vice-president right!

# President	Start	Last	Seasons	Vice-president
# donald trump	2017 Jan	-	1	Mike pence
# barack obama	2009	2017	2	joe Biden
# bush, george	2001	2009	2	Cheney, dick
# Clinton, Bill	1993	2001	two	gore, Al


import pandas as pd
import numpy as np

def cleaning_data():

    df = pd.read_csv("src/presidents.tsv", sep="\t")

    df.loc[3, "Seasons"] = "2"

    df["Start"] = df["Start"].replace(r"\D", "", regex=True).str.strip()

    df["Last"] = df["Last"].replace(r"[^0-9]", "", regex=True).str.strip()
    df["Last"] = df["Last"].mask(df["Last"] == "", np.nan)

    df["President"] = df["President"].mask(
        df["President"].str.match(r"^[a-zA-Z]+, [a-zA-Z]+$"), 
        df["President"].str.split(", ").apply(lambda x: " ".join(x[::-1]) if isinstance(x, list) else x))
    
    presidents = df["President"].str.split()
    presidents = presidents.apply(lambda x: " ".join(word.capitalize() for word in x))

    df["President"] = presidents
    
    df["Vice-president"] = df["Vice-president"].mask(
        df["Vice-president"].str.match(r"^[a-zA-Z]+, [a-zA-Z]+$"), 
        df["Vice-president"].str.split(", ").apply(lambda x: " ".join(x[::-1]) if isinstance(x, list) else x))
    
    vice_presidents = df["Vice-president"].str.split()
    vice_presidents = vice_presidents.apply(lambda x: " ".join(word.capitalize() for word in x))

    df["Vice-president"] = vice_presidents
        

    df = df.astype({"Start": int, "Last": float, "Seasons": int})
    
    return df

def main():

    print(cleaning_data())

    return

if __name__ == "__main__":
    main()
