#!/usr/bin/env python3

# Exercise 5.1 (split date continues)
# Write function split_date_continues that does

# read the bicycle data set
# clean the data set of columns/rows that contain only missing values
# drops the Päivämäärä column and replaces it with its splitted components as before
# Use the concat function to do this. The function should return a DataFrame with 25 columns (first five related to the date and then the rest 20 concerning the measument location.

# Hint: You may use your solution or the model solution from exercise 16 of the previous set as a starting point.

import pandas as pd


def split_date(df):
    return df

def split_date_continues():
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

    df = df.drop(columns=["Päivämäärä"])

    df_concat = pd.concat([dates, df], axis=1)

    df_concat.dropna(how='all', inplace=True)
    df_concat.dropna(how='all', axis=1, inplace=True)

    df_concat = df_concat.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})

    return df_concat

def main():
    df = split_date_continues()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())


if __name__ == "__main__":
    main()
