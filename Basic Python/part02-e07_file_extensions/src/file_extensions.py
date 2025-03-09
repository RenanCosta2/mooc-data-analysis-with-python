#!/usr/bin/env python3

# Exercise 2.7 (file extensions)
# This exercise can give two points at maximum!

# Part 1.

# Write function file_extensions that gets as a parameter a filename. It should read through the lines from this file. Each line contains a filename. Find the extension for each filename. The function should return a pair, where the first element is a list containing all filenames with no extension (with the preceding period (.) removed). The second element of the pair is a dictionary with extensions as keys and corresponding values are lists with filenames having that extension.

# Sounds a bit complicated, but hopefully the next example will clarify this. If the file contains the following lines

# file1.txt
# mydocument.pdf
# file2.txt
# archive.tar.gz
# test
# then the return value should be the pair: (["test"], { "txt" : ["file1.txt", "file2.txt"], "pdf" : ["mydocument.pdf"], "gz" : ["archive.tar.gz"] } )

# Part 2.

# Write a main method that calls the file_extensions function with "src/filenames.txt" as the argument. Then print the results so that for each extension there is a line consisting of the extension and the number of files with that extension. The first line of the output should give the number of files without extensions.

# With the example in part 1, the output should be

# 1 files with no extension
# gz 1
# pdf 1
# txt 2
# Had there been no filenames without extension then the first line would have been 0 files with no extension. In the printout list the extensions in alphabetical order.

import re
from collections import defaultdict

def file_extensions(filename):

    with open(filename, 'r') as f:
        no_extensions = []
        with_extensions = defaultdict(list)

        for line in f:
            line = line.strip()

            match = re.match(r"(.*)\.([\w]+$)", line)
            if match:
                extension = match.group(2)
                if extension not in with_extensions:
                    with_extensions[extension].append(line)
                else:
                    with_extensions[extension].append(line)
            else:
                no_extensions.append(line)

    with_extensions = dict(sorted(with_extensions.items()))

    return (no_extensions, with_extensions)

def main():
    
    files = file_extensions("src/filenames.txt")

    print(f'{len(files[0])} files with no extension')
    
    for file in files[1]:
        print(f'{file} {len(files[1].get(file))}')

if __name__ == "__main__":
    main()
