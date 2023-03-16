import numpy as np
from numpy.random import rand

knots = rand(100, 2)

np.savetxt('knots.txt', knots, delimiter=' ', newline='\n', fmt='%f')
