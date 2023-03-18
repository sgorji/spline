import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
from spline import Interpolator

interpolator = Interpolator()
points = rand(1000)
values = list(map(interpolator.interp, points))

# correctness
plt.figure(figsize=(15, 10))
plt.scatter(points, values)
plt.scatter(interpolator.knots[:, 0], interpolator.knots[:, 1], )
plt.show()
