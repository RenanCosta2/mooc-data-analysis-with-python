#!/usr/bin/env python3

# Exercise 1.15 (two dice comprehension)
# Redo the earlier exercise which printed all the pairs of two dice results that sum to 5. But this time use a list comprehension. Print one pair per line.

def main():
    
    pairs = ((dice_1+1, dice_2+1) for dice_1 in range(6) 
                                    for dice_2 in range(6)
                                    if (dice_1+1) + (dice_2+1) == 5)

    for pair in pairs:
        print(pair)

if __name__ == "__main__":
    main()
