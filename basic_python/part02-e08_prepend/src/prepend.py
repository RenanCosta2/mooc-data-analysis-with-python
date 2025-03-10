#!/usr/bin/env python3

# Exercise 2.8 (prepend)
# Create a class called Prepend. We create an instance of the class by giving a string as a parameter to the initializer. The initializer stores the parameter in an instance attribute start. The class also has a method write(s) which prints the string s prepended with the start string. An example of usage:


# p = Prepend("+++ ")
# p.write("Hello")
# Will print

# +++ Hello
# Try out using the class from the main function.

class Prepend(object):
    
    def __init__(self, string):
        self.string = string

    def write(self, s):
        print(self.string + s)
        


def main():
    p = Prepend("+++ ")
    p.write("Hello")

if __name__ == "__main__":
    main()
