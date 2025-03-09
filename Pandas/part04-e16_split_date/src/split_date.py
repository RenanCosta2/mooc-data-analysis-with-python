#!/usr/bin/env python3

# Exercise 4.16 (split date)
# Read again the bicycle data set from src folder, and clean it as in the earlier exercise. Then split the Päivämäärä column into a DataFrame with five columns with column names Weekday, Day, Month, Year, and Hour. Note that you also need to to do some conversions. To get Hours, drop the colon and minutes. Convert field Weekday according the following rule:

# ma -> Mon
# ti -> Tue
# ke -> Wed
# to -> Thu
# pe -> Fri
# la -> Sat
# su -> Sun
# Convert the Month column according to the following mapping

# tammi 1
# helmi 2
# maalis 3
# huhti 4
# touko 5
# kesä 6
# heinä 7
# elo 8
# syys 9
# loka 10
# marras 11
# joulu 12
# Create function split_date that does the above and returns a DataFrame with five columns. You may want to use the map method of Series objects.

# So the first element in the Päivämäärä column of the original data set should be converted from ke 1 tammi 2014 00:00 to Wed 1 1 2014 0 . Test your solution from the main function.

import pandas as pd
import numpy as np


def split_date():

    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")

    dates = df["Päivämäärä"]
    weekday_map = {
        "ma": "Mon", "ti": "Tue", "ke": "Wed",
        "to": "Thu", "pe": "Fri", "la": "Sat", "su": "Sun"
    }

    month_map = {
        "tammi": "1", "helmi": "2", "maalis": "3", "huhti": "4",
        "touko": "5", "kesä": "6", "heinä": "7", "elo": "8",
        "syys": "9", "loka": "10", "marras": "11", "joulu": "12"
    }

    dates = dates.replace(month_map, regex=True)
    dates = dates.replace(weekday_map, regex=True)

    dates = dates.str.replace(r":.*", '', regex=True)

    dates = dates.str.split(expand=True)

    dates.rename(columns={0: "Weekday", 1: "Day", 2: "Month", 3: "Year", 4: "Hour"}, inplace=True)

    dates.dropna(inplace=True)

    dates = dates.astype({"Day": int, "Month": int, "Year": int, "Hour": int})

    return dates

def main():

    print(split_date())

    return
       
if __name__ == "__main__":
    main()
