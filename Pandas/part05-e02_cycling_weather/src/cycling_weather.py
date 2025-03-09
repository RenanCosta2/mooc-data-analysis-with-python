#!/usr/bin/env python3

# Exercise 5.2 (cycling weather)
# Merge the processed cycling data set (from the previous exercise) and weather data set along the columns year, month, and day. Note that the names of these columns might be different in the two tables: use the left_on and right_on parameters. Then drop useless columns 'm', 'd', 'Time', and 'Time zone'.

# Write function cycling_weather that reads the data sets and returns the resulting DataFrame.

import pandas as pd


def cycling_weather():

    cycling = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")

    dates = cycling["Päivämäärä"]
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

    cycling = cycling.drop(columns=["Päivämäärä"])

    cycling_concat = pd.concat([dates, cycling], axis=1)

    cycling_concat.dropna(how='all', inplace=True)
    cycling_concat.dropna(how='all', axis=1, inplace=True)

    cycling_concat = cycling_concat.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})

    weather = pd.read_csv("src/kumpula-weather-2017.csv", sep=",")

    cycling_weather_df = pd.merge(cycling_concat, weather, left_on=["Year", "Month", "Day"], right_on=["Year", "m", "d"])

    cycling_weather_df.drop(columns=["m", "d", "Time", "Time zone"], inplace=True)

    return cycling_weather_df

def main():

    print(cycling_weather())

    return

if __name__ == "__main__":
    main()
