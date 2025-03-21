#!/usr/bin/env python3

# Exercise 4.15 (last week)
# This exercise can give two points at maximum!

# Write function last_week that reads the top40 data set mentioned in the above exercise. The function should then try to reconstruct the top40 list of the previous week based on that week's list. Try to do this as well as possible. You can fill the values that are impossible to reconstruct by missing value symbols. Your solution should work for a top40 list of any week. So don't rely on specific features of this top40 list. The column WoC means "Weeks on Chart", that is, on how many weeks this song has been on the top 40 list.

# Hint. First create the last week's top40 list of those songs that are also on this week's list. Then add those entries that were not on this week's list. Finally sort by position.

# Hint 2. The where method of Series and DataFrame can be useful. It can also be nested.

# Hint 3. Like in NumPy, you can use with Pandas the bitwise operators &, |, and ~. Remember that the bitwise operators have higher precedence than the comparison operations, so you may have to use parentheses around comparisons, if you combined result of comparisons with bitwise operators.

# You get a second point, if you get the columns LW and Peak Pos correct.

import pandas as pd
import numpy as np

def last_week():

    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")

    lw_df = df.copy()

    lw_df.replace(["New", "Re"], np.nan, inplace=True)
    lw_df.dropna(inplace=True)
    lw_df = lw_df.astype({"LW": int})

    lw_df["Peak Pos"] = lw_df["Peak Pos"].mask(
        (lw_df["Peak Pos"] == lw_df["Pos"]) & 
        ((lw_df["Peak Pos"] != lw_df["LW"])), 
        np.nan)

    lw_df.Pos = lw_df.LW
    lw_df.LW = np.nan
    lw_df = lw_df.astype({"Pos": int})

    lw_df["WoC"] = lw_df["WoC"].apply(lambda x: max(x - 1, 0))

    df_length = len(df)
    missing_indices = set(range(1, df_length + 1)) - set(lw_df['Pos'])

    missing_rows = pd.DataFrame(np.nan, index=list(missing_indices), columns=lw_df.columns)
    missing_rows['Pos'] = missing_rows.index
    lw_df = pd.concat([lw_df, missing_rows], ignore_index=True)

    lw_df.sort_values(by=['Pos'], inplace=True)

    return lw_df

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
