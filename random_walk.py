import random
#import numpy as np
import matplotlib.pyplot as plt

def randomWalk1D(number_of_walks, starting_point, boundary_condition, step_size):
	path = []
	probability = 0

	for i in range(number_of_walks):

		curr_point = starting_point
		curr_path = []
		while(True):
			d = random.randint(0,1)
			if curr_point in boundary_condition:
				probability = probability+ (curr_point/boundary_condition[1])
				#print(probability)
				break 
			if d>=0.5:
				curr_point = min(curr_point+step_size, boundary_condition[1])
			else:
				curr_point = max(curr_point-step_size, boundary_condition[0])
			curr_path.append(curr_point)
		path.append(curr_path)

		
	probability = probability/number_of_walks	
	return (path,probability)





