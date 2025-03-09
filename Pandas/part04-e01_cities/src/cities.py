#!/usr/bin/env python3

# Exercise 4.1 (cities)
# Write function cities that returns the following DataFrame of top Finnish cities by population:


#                  Population Total area
# Helsinki         643272     715.48
# Espoo            279044     528.03
# Tampere          231853     689.59
# Vantaa           223027     240.35
# Oulu             201810     3817.52

import pandas as pd

def cities():

    df_cities = pd.DataFrame([
        [643272, 715.48],
        [279044, 528.03],
        [231853, 689.59],
        [223027, 240.35],
        [201810, 3817.52]
    ], 
    columns=["Population", "Total area"], 
    index=["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"])

    return df_cities
    
def main():

    print(cities())
    return
    
if __name__ == "__main__":
    main()
