#!/usr/bin/env python3

# Exercise 5.13 (cycling weather continues)
# Write function cycling_weather_continues that tries to explain with linear regression the variable of a cycling measuring station's counts using the weather data from corresponding day. The function should take the name of a (cycling) measuring station as a parameter and return the regression coefficients and the score. In more detail:

# Read the weather data set from the src folder. Read the cycling data set from folder src and restrict it to year 2017. Further, get the sums of cycling counts for each day. Merge the two datasets by the year, month, and day. Note that for the above you need only small additions to the solution of exercise cycling_weather. After this, use forward fill to fill the missing values.

# In the linear regression use as explanatory variables the following columns 'Precipitation amount (mm)', 'Snow depth (cm)', and 'Air temperature (degC)'. Explain the variable (measuring station), whose name is given as a parameter to the function cycling_weather_continues. Fit also the intercept. The function should return a pair, whose first element is the regression coefficients and the second element is the score. Above, you may need to use the method reset_index (its counterpart is the method set_index).

# The output from the main function should be in the following form:


# Measuring station: x
# Regression coefficient for variable 'precipitation': x.x
# Regression coefficient for variable 'snow depth': x.x
# Regression coefficient for variable 'temperature': x.x
# Score: x.xx
# Use precision of one decimal for regression coefficients, and precision of two decimals for the score. In the main function test you solution using some measuring station, for example Baana.

# %%
import pandas as pd
from sklearn import linear_model

# %%
def cycling_weather_continues(station):

    weather = pd.read_csv("src/kumpula-weather-2017.csv", sep=",")
    cycling = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")

    cycling.dropna(how='all', inplace=True)
    cycling.dropna(how='all', axis=1, inplace=True)

    weekday_map = {
        "ma": "Mon", "ti": "Tue", "ke": "Wed",
        "to": "Thu", "pe": "Fri", "la": "Sat", "su": "Sun"
    }

    month_map = {
        "tammi": "1", "helmi": "2", "maalis": "3", "huhti": "4",
        "touko": "5", "kesä": "6", "heinä": "7", "elo": "8",
        "syys": "9", "loka": "10", "marras": "11", "joulu": "12"
    }

    dates = cycling["Päivämäärä"]
    dates.replace(month_map, regex=True, inplace=True)
    dates.replace(weekday_map, regex=True, inplace=True)
    dates.replace(r':.*', '', regex=True, inplace=True)
    dates = dates.str.split(expand=True)

    dates.rename(columns={0: "Weekday", 1: "Day", 2: "Month", 3: "Year", 4: "Hour"}, inplace=True)

    dates = dates.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})

    cycling.drop(columns="Päivämäärä", inplace=True)

    cycling = pd.concat([dates, cycling], axis=1)

    cycling_2017 = cycling[cycling["Year"] == 2017]

    cycling_by_day_2017 = cycling_2017.groupby(["Year", "Month", "Day"]).sum()
    cycling_by_day_2017.drop(columns=["Hour"], inplace=True)
    cycling_by_day_2017.reset_index(inplace=True)
    cycling_by_day_2017

    weather.rename(columns={"m": "Month", "d": "Day"}, inplace=True)
    
    cycling_weather = pd.merge(cycling_by_day_2017, weather, how="outer")
    cycling_weather.fillna(method='ffill', inplace=True)

    features = cycling_weather[[
        "Precipitation amount (mm)",
        "Snow depth (cm)",
        "Air temperature (degC)"
    ]]

    reg = linear_model.LinearRegression()
    reg.fit(features, cycling_weather[station])
    score = reg.score(features, cycling_weather[station])

    intercept, coefs = reg.intercept_, reg.coef_

    return coefs, score
# %%

def main():

    station = "Ratapihantie"

    coefs, score = cycling_weather_continues(station)

    print(f"Measuring station: {station}")
    print(f"Regression coefficient for variable 'precipitation': {coefs[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {coefs[1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {coefs[2]:.1f}")
    print(f"Score: {score:.2f}")

    return

if __name__ == "__main__":
    main()
