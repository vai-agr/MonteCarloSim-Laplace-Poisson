import random
#import numpy as np
#import matplotlib.pyplot as plt

def randomWalk1D(number_of_walks, starting_point, length, boundary_condition, step_size=1):
	path = []
	curr_point = starting_point
	for i in range(number_of_walks):
		d = random.randint(0,1)
		if d>=0.5:
			curr_point = min(curr_point+step_size, boundary_condition[1])
		else:
			curr_point = max(curr_point-step_size, boundary_condition[0])
		path.append(curr_point)

	return path





