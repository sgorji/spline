import numpy as np
import pandas as pd

# reading input knots
knots = np.loadtxt('knots.txt')

# sorting input knots by their x value (if necessary)
sort_index = np.argsort(knots[:, 0])
knots = knots[sort_index]

# binary search

# interpolation function
