# A = pi*r^2
# A = 4r^2
# is Value of pi/4

import numpy as np
import random

# Using Area calculation
num_pts = 1000000

circle = 0
square = 0
for i in range(num_pts):
	x = np.array(random.uniform(-1, 1))
	y = np.array(random.uniform(-1, 1))
	# Adding for pts inside square or circle based on radius distance
	rad = x ** 2 + y ** 2
	if rad <= 1:
		circle += 1
	square += 1

	pi = (circle / square) * 4

print("pi={}".format(pi))