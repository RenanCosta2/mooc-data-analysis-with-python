#!/usr/bin/env python3

# Exercise 1.10 (detect ranges)
# Create a function named detect_ranges that gets a list of integers as a parameter. The function should then sort this list, and transform the list into another list where pairs are used for all the detected intervals. So 3,4,5,6 is replaced by the pair (3,7). Numbers that are not part of any interval result just single numbers. The resulting list consists of these numbers and pairs, separated by commas. An example of how this function works:

# print(detect_ranges([2,5,4,8,12,6,7,10,13]))
# [2,(4,9),10,(12,14)]
# Note that the second element of the pair does not belong to the range. This is consistent with the way Python's range function works. You may assume that no element in the input list appears multiple times.

def detect_ranges(L):

    L_sorted = sorted(L)

    new_L = []
    lower = L_sorted[0]
    higher = lower

    for number in L_sorted[1:]:
        
        if(number == (higher+1)):
            higher = number
        else:
            if lower == higher:
                new_L.append(lower)
            else:
                new_L.append((lower, higher+1))
            
            lower = number
            higher = number

    
    if lower == higher:
        new_L.append(lower)
    else:
        new_L.append((lower, higher+1))

    return new_L

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
