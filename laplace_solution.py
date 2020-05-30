import random_walk as rw       #imported random_walk.py for using the randomWalk1D function
import matplotlib.pyplot as plt   #for graphing functions

number_of_walks = 200		 #Number of random walks for each point
step_size = 1				 #Distance between each point = 1cm ie 10 divisions
length = 20					 #Distance between the plates of the capacitor = 10 cm	
boundary_voltages = [0,10]    #Voltages of the two plates of the capacitor in Volts

if __name__ == "__main__":		#the main part

	P_a =[]
	points = [i for i in range(0,length+step_size,step_size)]
	for point in points:

		(ans,prob) = rw.randomWalk1D(number_of_walks,point,[0,length],step_size)  #length starts at 0
		#print(ans)
		P_a.append(prob)				#Probability of reaching boundary(whilst Random Walking) for all the points

	print(P_a)
	voltage_final = [(i*boundary_voltages[1]+ (1-i)*boundary_voltages[0]) for i in P_a]
	voltage_actual = [boundary_voltages[0]+(i/length)*(boundary_voltages[1]- boundary_voltages[0]) for i in points]

	p1 = plt.plot(voltage_final, marker='o', markersize=4)
	p2 = plt.plot(voltage_actual)
	plt.title("LAPLACE EQUATION")
	plt.xlabel("Distance from the low voltage capacitor plate (in cm)")
	plt.ylabel("Voltage (in Volts)")
	plt.xticks(range(0,length+step_size,2*step_size))
	plt.legend((p1[0], p2[0]),('Calculated Voltage', 'Actual Voltage'))
	plt.show()