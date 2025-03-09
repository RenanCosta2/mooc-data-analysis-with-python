#!/usr/bin/env python3

# Exercise 1.20 (usemodule)
# Create your own module as file triangle.py in the src folder. The module should contain two functions:

# hypotenuse which returns the length of the hypotenuse when given the lengths of two other sides of a right-angled triangle
# area which returns the area of the right-angled triangle, when two sides, perpendicular to each other, are given as parameters.
# Make sure both the functions and the module have descriptive docstrings. Add also the __version__ and __author__ attributes to the module. Call both your functions from the main function (which is in file usemodule.py).

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    print(triangle.hypotenuse(4, 3))
    print(triangle.area(4, 3))

if __name__ == "__main__":
    main()
