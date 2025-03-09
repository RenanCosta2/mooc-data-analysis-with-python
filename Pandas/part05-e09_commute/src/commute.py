#!/usr/bin/env python3

# Exercise 5.9 (commute)
# In function commute do the following:

# Use the function bicycle_timeseries to get the bicycle data. Restrict to August 2017, group by the weekday, aggregate by summing. Set the Weekday column to numbers from one to seven. Then set the column Weekday as the (row) index. Return the resulting DataFrame from the function.

# In the main function plot the DataFrame. Xticklabels should be the weekdays. Don't forget to call show function!

# If you want the xticklabels to be ['Mon', 'Tue', 'Wed', 'Thu', 'Fr', 'Sat', 'Sun'] instead of numbers (1,..,7), then it may get a bit messy. There seems to be a problem with non-numeric x values. You could try the following after plotting, but you don't have to:

# weekdays="x mon tue wed thu fri sat sun".title().split()
# plt.gca().set_xticklabels(weekdays)

import pandas as pd
import matplotlib.pyplot as plt

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
    dates = dates.str.replace(r":.*", '', regex=True)

    dates = dates.str.split(expand=True)
    dates.rename(columns={0: "Weekday", 1: "Day", 2: "Month", 3: "Year", 4: "Hour"}, inplace=True)

    datetime = pd.to_datetime(dates[["Year", "Month", "Day", "Hour"]], dayfirst=True)

    dates.drop(["Day", "Month", "Year", "Hour"], axis=1, inplace=True)

    df = pd.concat([datetime, dates, df], axis=1)

    df.drop(["Päivämäärä"], axis=1, inplace=True)

    df = df.set_index(0)

    return df

def commute():

    bicycle_data = bicycle_timeseries()

    august_2017 = bicycle_data["2017-08-01":"2017-08-31"]
    weekday_map = {
        "Mon": 1, "Tue": 2, "Wed": 3,
        "Thu": 4, "Fri": 5, "Sat": 6, "Sun": 7
    }

    august_2017.loc[:, "Weekday"] = august_2017["Weekday"].map(weekday_map)

    group_by_weekday = august_2017.groupby("Weekday")

    group_by_weekday_sum = group_by_weekday.sum()

    return group_by_weekday_sum
    
def main():
    
    plt.plot(commute())
    
    plt.show()


if __name__ == "__main__":
    main()
