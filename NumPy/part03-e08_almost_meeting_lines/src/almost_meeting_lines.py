#!/usr/bin/python3

# Exercise 3.8 (almost meeting lines)
# In the earlier "meeting lines" exercise there is a problem if the lines don't meet at all. Extend that solution so that it tells the meeting point if it exists, and otherwise finds the point that is closest to both lines. You can use the numpy.linalg.lstsq for this.

# Example of usage:


# (x, y), exact = almost_meeting_lines(1, 2, -1, 0)
# print(x, y, exact)
# -1.000000 1.000000 True

import numpy as np

def almost_meeting_lines(a1, b1, a2, b2):

    A = np.array([[a1, -1], [a2, -1]])
    B = np.array([-b1, -b2])

    try:
        return np.linalg.solve(A, B), True
    except:
        return np.linalg.lstsq(A, B)[0], False

def main():
    a1=1
    b1=2
    a2=-1
    b2=0

    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")

    a1=a2=1
    b1=2
    b2=-2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b1)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    a2=1
    b2=1
    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

if __name__ == "__main__":
    main()
