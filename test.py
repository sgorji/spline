import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
from spline import Interpolator
from time import time

# performance
results = {}
for knots_count in [1000, 2000, 5000, 10000]:
    results[knots_count] = {}
    for points_count in [1000, 2000, 5000, 10000]:
        interpolator = Interpolator(knots_count)
        points = rand(points_count)
        start = time()
        values = list(map(interpolator.interp, points))
        end = time()
        results[knots_count][points_count] = end - start

plt.figure(figsize=(15, 10))
for knots_count in results:
    plt.plot(list(results[knots_count].keys()),
             list(results[knots_count].values()))
plt.legend(
    [f'knots = {knots}' for knots in results], loc="lower right")
plt.show()


# correctness
interpolator = Interpolator()
points = rand(1000)
values = list(map(interpolator.interp, points))

plt.figure(figsize=(15, 10))
plt.scatter(points, values)
plt.scatter(interpolator.knots[:, 0], interpolator.knots[:, 1], )
plt.show()
