import numpy as np
from numpy.random import rand
import pandas as pd


class Interpolator():

    def __init__(self, number_of_knots=0):
        if not number_of_knots:
            # reading input knots
            knots = np.loadtxt('knots.txt')
        else:
            knots = rand(number_of_knots, 2)

        # sorting input knots by their x value (if necessary)
        sort_index = np.argsort(knots[:, 0])
        self.knots = knots[sort_index]

    # binary search
    # def binary_search(left, right, x):
    #     if (right <= left + 1):
    #         return left
    #     middle = (left + right) // 2
    #     if (x > knots[middle][0]):
    #         return binary_search(middle, right, x)
    #     else:
    #         return binary_search(left, middle, x)

    def binary_search(self, x):
        '''binary search  function to find the location of x among knots'''
        left = 0
        right = len(self.knots) - 1

        while left <= right:
            middle = (left + right) // 2
            if (x > self.knots[middle][0]):
                left = middle + 1
            else:
                right = middle - 1
        return middle

    def interp(self, x):
        '''interpolation function'''
        position = self.binary_search(x)

        # the position variable pinpoints the location of x among the knots
        # now depending on the relation of the knots[position] with x
        # the algorithm decides the value for x
        # for edge cases where x is smaller (larger) than all the knots its
        # value mimics the closest knot, otherwise, it returns a linear
        # interpolation of the values of its adjacent knots
        if x > self.knots[position][0]:
            if position >= (len(self.knots) - 1):
                return self.knots[-1][1]
            else:
                diff = self.knots[position + 1] - self.knots[position]
                return self.knots[position][1] + diff[1] * (x - self.knots[position][0]) / diff[0]
        else:
            if position <= 0:
                return self.knots[0][1]
            else:
                diff = self.knots[position] - self.knots[position - 1]
                return self.knots[position - 1][1] + diff[1] * (x - self.knots[position - 1][0]) / diff[0]
