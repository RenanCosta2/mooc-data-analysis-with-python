#!/usr/bin/env python3

# Exercise 1.5 (two dice)
# Let us consider throwing two dice. (A dice can give a value between 1 and 6.) Use two nested for loops in the main function to iterate through all possible combinations the pair of dice can give. There are 36 possible combinations. Print all those combinations as (ordered) pairs that sum to 5. For example, your printout should include the pair (2,3). Print one pair per line.

def main():
    
    for dice_1 in range(6):
        for dice_2 in range(6):
            if (dice_1+1) + (dice_2+1) == 5:
                print(f"({dice_1+1}, {dice_2+1})")

if __name__ == "__main__":
    main()
