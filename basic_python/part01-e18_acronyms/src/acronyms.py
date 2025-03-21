#!/usr/bin/env python3

# Exercise 1.18 (acronyms)
# Write function acronyms which takes a string as a parameter and returns a list of acronyms. A word is an acronym if it has length at least two, and all its characters are in uppercase. Notice an acronym can also have numbers. Before acronym detection, delete punctuation with the strip method.

# Test this function in the main function with the following call:


# print(acronyms("""For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."""))
# This should return ['EU', 'GDPR', 'IBM', 'IBM', 'EEA', 'EEA', 'IBM', 'PO', 'PO6', '3AU']

def acronyms(s):

    s = s.split()

    acronyms_words = []

    for word in s:
        if word.isupper():
            word = word.strip("(),.;:!?")
            acronyms_words.append(word)

    return acronyms_words

def main():
    print(acronyms("""For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."""))


if __name__ == "__main__":
    main()
