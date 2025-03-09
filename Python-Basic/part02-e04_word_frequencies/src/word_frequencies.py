#!/usr/bin/env python3

# Exercise 2.4 (word frequencies)
# Create function word_frequencies that gets a filename as a parameter and returns a dict with the word frequencies. In the dictionary the keys are the words and the corresponding values are the number of times that word occurred in the file specified by the function parameter. Read all the lines from the file and split the lines into words using the split() method. Further, remove punctuation from the ends of words using the strip("""!"#$%&'()*,-./:;?@[]_""") method call.

# Test this function in the main function using the file alice.txt. In the output, there should be a word and its count per line separated by a tab:

# The     64
# Project 83
# Gutenberg   26
# EBook   3
# of      303

import os

def word_frequencies(filename):

    words_dict = {}

    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                word = word.strip("""!"#$%&'()*,-./:;?@[]_""")

                if word not in words_dict:
                    words_dict[word] = 1
                else:
                    words_dict[word] = words_dict.get(word)+1

    return words_dict

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, "alice.txt")
    dict_words = word_frequencies(filename)

    print(dict_words)

if __name__ == "__main__":
    main()
