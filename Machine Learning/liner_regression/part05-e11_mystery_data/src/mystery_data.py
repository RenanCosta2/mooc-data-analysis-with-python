#!/usr/bin/env python3

# Exercise 5.11 (mystery data)
# Read the tab separated file mystery_data.tsv. Its first five columns define the features, and the last column is the response. Use scikit-learn's LinearRegression to fit this data. Implement function mystery_data that reads this file and learns and returns the regression coefficients for the five features. You don't have to fit the intercept. The main method should print output in the following form:


# Coefficient of X1 is ...
# Coefficient of X2 is ...
# Coefficient of X3 is ...
# Coefficient of X4 is ...
# Coefficient of X5 is ...
# Which features you think are needed to explain the response Y?

# %%

import pandas as pd
from sklearn.linear_model import LinearRegression
# %%
def mystery_data():

    # %%
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    df

    #%%

    features = ["X1", "X2", "X3", "X4", "X5"]

    X = df[features]
    
    # %%
    reg = LinearRegression(fit_intercept=False)
    reg.fit(X, df["Y"])
    reg.coef_

    # %%
    return reg.coef_

def main():
    # %%
    coefficients = mystery_data()
    coefficients
    # %%
    # print the coefficients here
    for i, coefficient in enumerate(coefficients):
        print(f"Coefficient of X{i} is {coefficient}")
    
# %%    
if __name__ == "__main__":
    main()
