#!/usr/bin/env python3

# Everything after a hash sign (#) is considered a comment in Python

# The print statement could be written on the top-level (zero indentation),
# but here we have put it inside the main function.
# This enables TestMyCode (TMC) framework to work correctly.

# In more complicated programs it is good practise not to clutter the top-level of the program
# by using a main function as here.

# Exercise 1.1 (hello world)
# Fill in the missing piece in the solution stub file hello_world.py in folder src to make it print the following:

# Hello, world!
# Make sure you use correct indenting. You can run it with command python3 src/hello_world.py. If the output looks good, then you can test it with command tmc test. If the tests pass, submit your solution to the server with command tmc submit.

def main():
    # Enter your code here, this is the correct indentation

    print("Hello, world!")

# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
    main()
