import numpy as np
import pandas as pd

# reading input knots
knots = np.loadtxt('knots.txt')

# sorting input knots by their x value (if necessary)
sort_index = np.argsort(knots[:, 0])
knots = knots[sort_index]

# binary search


# def binary_search(left, right, x):
#     if (right <= left + 1):
#         return left
#     middle = (left + right) // 2
#     if (x > knots[middle][0]):
#         return binary_search(middle, right, x)
#     else:
#         return binary_search(left, middle, x)


def binary_search(x):
    left = 0
    right = len(knots) - 1

    while left <= right:
        middle = (left + right) // 2
        if (x > knots[middle][0]):
            left = middle + 1
        else:
            right = middle - 1
    return middle

# interpolation function


def interp(x):
    position = binary_search(x)

    # the position variable pinpoints the location of x among the knots
    # now depending on the relation of the knots[position] with x
    # the algorithm decides the value for x
    # for edge cases where x is smaller (larger) than all the knots its
    # value mimics the closest knot, otherwise, it returns a linear
    # interpolation of the values of its adjacent knots
    if x > knots[position][0]:
        if position >= (len(knots) - 1):
            return knots[-1][1]
        else:
            diff = knots[position + 1] - knots[position]
            return knots[position][1] + diff[1] * (x - knots[position][0]) / diff[0]
    else:
        if position <= 0:
            return knots[0][1]
        else:
            diff = knots[position] - knots[position - 1]
            return knots[position - 1][1] + diff[1] * (x - knots[position - 1][0]) / diff[0]
