#!/usr/bin/env python3

# Exercise 2.1 (integers in brackets)
# Write function integers_in_brackets that finds from a given string all integers that are enclosed in brackets.

# Example run: integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx") returns [12, -43, 12]. So there can be whitespace between the number and the brackets, but no other character besides those that make up the integer.

# Test your function from the main function.

import re

def integers_in_brackets(s):

    integers = re.findall(r'\[\s*([+-]?\d+)\s*\]', s)
    return list(map(int, integers))

def main():
    integers = integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx")

    print(integers)

if __name__ == "__main__":
    main()
