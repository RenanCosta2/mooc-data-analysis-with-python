#!/usr/bin/env python3

# Exercise 1.3 (multiplication)
# Make a program that gives the following output. You should use a for loop in your solution.

# 4 multiplied by 0 is 0
# 4 multiplied by 1 is 4
# 4 multiplied by 2 is 8
# 4 multiplied by 3 is 12
# 4 multiplied by 4 is 16
# 4 multiplied by 5 is 20
# 4 multiplied by 6 is 24
# 4 multiplied by 7 is 28
# 4 multiplied by 8 is 32
# 4 multiplied by 9 is 36
# 4 multiplied by 10 is 40

def main():
    # Enter your solution here

    for number in range(11):
        print(f"4 multiplied by {number} is {number * 4}")

if __name__ == "__main__":
    main()
