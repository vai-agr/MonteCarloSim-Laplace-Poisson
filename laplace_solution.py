#Convert everything in SI units

import random_walk as rw
import matplotlib.pyplot as plt

number_of_walks = 400		 #number of random walks for each point
step_size = 1				 #distance between each point 
length = 10					 #Distance between the plates of the capacitor in cm	
boundary_voltages = [0,5]   #Voltages of the two plates of the capacitor in Volts


if __name__ == "__main__":

	P_a =[]
	for point in range(0,length,step_size):

		(ans,prob) = rw.randomWalk1D(number_of_walks,point,[0,length],step_size)  #length starts at 0
		#print(ans)
		P_a.append(prob)
	print(P_a)
	voltage_final = [(i*boundary_voltages[1]+ (1-i)*boundary_voltages[0]) for i in P_a]
	plt.plot(voltage_final)
	plt.show()