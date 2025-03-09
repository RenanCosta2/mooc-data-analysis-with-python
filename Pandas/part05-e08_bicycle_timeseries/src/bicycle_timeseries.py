#!/usr/bin/env python3

# Exercise 5.8 (bicycle timeseries)
# Write function bicycle_timeseries that

# reads the data set
# cleans it
# turns its Päivämäärä column into (row) DatetimeIndex (that is, to row names) of that DataFrame
# returns the new DataFrame

import pandas as pd


def bicycle_timeseries():

    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")

    df.dropna(how='all',inplace=True)
    df.dropna(how='all', axis=1, inplace=True)

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

    dates = pd.to_datetime(dates, dayfirst=True)

    df["Päivämäärä"] = dates

    df = df.set_index("Päivämäärä")

    return df


def main():
    
    print(bicycle_timeseries())

if __name__ == "__main__":
    main()
