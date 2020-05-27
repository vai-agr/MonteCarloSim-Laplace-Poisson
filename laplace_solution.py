import random_walk as rw
import matplotlib.pyplot as plt

number_of_walks = 100		 #Number of random walks for each point
step_size = 1				 #Distance between each point = 1cm ie 10 divisions
length = 10					 #Distance between the plates of the capacitor = 10 cm	
boundary_voltages = [0,5]    #Voltages of the two plates of the capacitor in Volts

if __name__ == "__main__":

	P_a =[]
	points = [i for i in range(0,length+step_size,step_size)]
	for point in points:

		(ans,prob) = rw.randomWalk1D(number_of_walks,point,[0,length],step_size)  #length starts at 0
		#print(ans)
		P_a.append(prob)
	print(P_a)
	voltage_final = [(i*boundary_voltages[1]+ (1-i)*boundary_voltages[0]) for i in P_a]
	voltage_actual = [boundary_voltages[0]+(i/length)*(boundary_voltages[1]- boundary_voltages[0]) for i in points]
	plt.plot(voltage_final, marker='o')
	plt.plot(voltage_actual)
	plt.show()