#!/usr/bin/env python3

# Exercise 2.2 (file listing)
# The file src/listing.txt contains a list of files with one line per file. Each line contains seven fields: access rights, number of references, owner's name, name of owning group, file size, date, filename. These fields are separated with one or more spaces. Note that there may be spaces also within these seven fields.

# Write function file_listing that loads the file src/listing.txt. It should return a list of tuples (size, month, day, hour, minute, filename). Use regular expressions to do this (either match, search, findall, or finditer method).

# An example: for line

# -rw-r--r-- 1 jttoivon hyad-all   25399 Nov  2 21:25 exception_hierarchy.pdf
# the function should create the tuple (25399, "Nov", 2, 21, 25, "exception_hierarchy.pdf").

import re
import os


def file_listing():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, "listing.txt")

    list = []
    with open(filename, "r") as f:
        for line in f:
            mo = re.search(r'(\d+)\s*([a-zA-Z]{3})\s*(\d{1,2})\s*(\d{2}):(\d{2})\s*([\w\.]+)', line)
            
            size = int(mo.group(1))
            month = mo.group(2)
            day = int(mo.group(3))
            hour = int(mo.group(4))
            minute = int(mo.group(5))
            file = mo.group(6)

            tuple = (size, month, day, hour, minute, file)
            list.append(tuple)

    return list

def main():
    
    print(file_listing())

if __name__ == "__main__":
    main()
