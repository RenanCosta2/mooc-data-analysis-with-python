#!/usr/bin/env python3

# Exercise 1.4 (multiplication table)
# In the main function print a multiplication table, which is shown below:

#    1   2   3   4   5   6   7   8   9  10
#    2   4   6   8  10  12  14  16  18  20
#    3   6   9  12  15  18  21  24  27  30
#    4   8  12  16  20  24  28  32  36  40
#    5  10  15  20  25  30  35  40  45  50
#    6  12  18  24  30  36  42  48  54  60
#    7  14  21  28  35  42  49  56  63  70
#    8  16  24  32  40  48  56  64  72  80
#    9  18  27  36  45  54  63  72  81  90
#   10  20  30  40  50  60  70  80  90 100
# For example at row 4 and column 9 we have 4*9=36.

# Use two nested for loops to achive this. Note that you can use the following form to stop the print function from automatically starting a new line:


# print("text", end="")
# print("more text")
# textmore text
# Print the numbers in a field with width four, so that the numbers are nicely aligned. For instructions on how adjust the field width refer to pyformat.info.

def main():
    
    for i in range(10):
        for j in range(10):
            print((i+1) * (j+1), end=" ")
        print()

if __name__ == "__main__":
    main()
