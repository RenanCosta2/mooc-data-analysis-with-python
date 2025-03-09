#!/usr/bin/env python3

# Exercise 1.19 (sum equation)
# Write a function sum_equation which takes a list of positive integers as parameters and returns a string with an equation of the sum of the elements.

# Example: sum_equation([1,5,7]) returns "1 + 5 + 7 = 13" Observe, the spaces should be exactly as shown above. For an empty list the function should return the string "0 = 0".

def sum_equation(L):

    L_string = list(map(str, L))

    sum_string = " + ".join(L_string)

    sum_string += f" = {sum(L)}"

    if not L:
        sum_string = f"0 = {sum(L)}"

    return sum_string

def main():
    sum_string = sum_equation([1,5,7])
    print(sum_string)

if __name__ == "__main__":
    main()
