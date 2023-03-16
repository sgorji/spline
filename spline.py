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
    return left

# interpolation function
