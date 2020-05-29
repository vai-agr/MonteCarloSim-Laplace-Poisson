import random                      # for random number generating functions
#import numpy as np 
import matplotlib.pyplot as py      #graph plotting library of python

#function for a random walk in 1D with given parameters.
def randomWalk1D(number_of_walks, starting_point, boundary_condition, step_size): 
	path = []																	  
	probability = 0

	for i in range(number_of_walks):

		curr_point = starting_point
		curr_path = []
		while(True):
			d = random.randint(0,1)     #generates random integers between 0 and 1
			if curr_point in boundary_condition:
				probability = probability+ (curr_point/boundary_condition[1])
				#print(probability)
				break 
			if d==1:                #if d=1, move forward
				curr_point = min(curr_point+step_size, boundary_condition[1])
			else:                   #if d=0, move backward
				curr_point = max(curr_point-step_size, boundary_condition[0])
			curr_path.append(curr_point)    #stores one random walk
		path.append(curr_path)      #stores the complete path for all random walks

		
	probability = probability/number_of_walks	#probability of reaching the right boundary
	return (path,probability)                   #returns the path array and the probability array





