#!/usr/bin/env python3

# Exercise 1.9 (merge)
# Suppose we have two lists L1 and L2 that contain integers which are sorted in ascending order. Create a function merge that gets these lists as parameters and returns a new sorted list L that has all the elements of L1 and L2. So, len(L) should equal to len(L1)+len(L2). Do this using the fact that both lists are already sorted. You can’t use the sorted function or the sort method in implementing the merge method. You can however use these sorted in the main function for creating inputs to the merge function. Test with a couple of examples in the main function that your solution works correctly.

# Note: In Python argument lists are passed by reference to the function, they are not copied! Make sure you don't modify the original lists of the caller.

def merge(L1, L2):
    L = []
    
    i, j = 0, 0
    
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            L.append(L1[i])
            i += 1
        else:
            L.append(L2[j])
            j += 1
    
    while i < len(L1):
        L.append(L1[i])
        i += 1
    
    while j < len(L2):
        L.append(L2[j])
        j += 1

    return L

def main():
    
    L1 = [1, 3, 5, 7]
    L2 = [2, 4, 6, 8]
    print(merge(L1, L2))
    
    L1 = [10, 20, 30]
    L2 = [15, 25, 35]
    print(merge(L1, L2))

if __name__ == "__main__":
    main()
