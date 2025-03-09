#!/usr/bin/env python3

# Exercise 5.4 (cyclists per day)
# This exercise can give two points at maximum!

# Part 1.

# Read, clean and parse the bicycle data set as before. Group the rows by year, month, and day. Get the sum for each group. Make function cyclists_per_day that does the above. The function should return a DataFrame. Make sure that the columns Hour and Weekday are not included in the returned DataFrame.

# Part 2.

# In the main function, using the function cyclists_per_day, get the daily counts. The index of the DataFrame now consists of tuples (Year, Month, Day). Then restrict this data to August of year 2017, and plot this data. Don't forget to call the plt.show function of matplotlib. The x-axis should have ticks from 1 to 31, and there should be a curve to each measuring station. Can you spot the weekends?

import pandas as pd
import matplotlib.pyplot as plt


def cyclists_per_day():

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

    group_cycling = cycling_concat.groupby(['Year', 'Month', 'Day']).sum()

    group_cycling.drop(columns=["Weekday", "Hour"],errors="ignore", inplace=True)

    return group_cycling
    
def main():

    day_count = cyclists_per_day()

    df_august_2017 = day_count.loc[(2017, 8)]

    plt.plot(df_august_2017)

    plt.show()

    print(df_august_2017)

    return

if __name__ == "__main__":
    main()
