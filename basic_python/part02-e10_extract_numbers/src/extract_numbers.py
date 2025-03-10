#!/usr/bin/env python3

# Exercise 2.10 (extract numbers)
# Write a function extract_numbers that gets a string as a parameter. It should return a list of numbers that can be both ints and floats. Split the string to words at whitespace using the split() method. Then iterate through each word, and initially try to convert to an int. If unsuccesful, then try to convert to a float. If not a number then skip the word.

# Example run: print(extract_numbers("abd 123 1.2 test 13.2 -1")) will return [123, 1.2, 13.2, -1]

def extract_numbers(s):

    s = s.split()
    numbers = []

    for word in s:
        try:
            num = int(word)
            numbers.append(num)
        except ValueError:
            try:
                num = float(word)
                numbers.append(num)
            except ValueError:
                continue

    return numbers

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
