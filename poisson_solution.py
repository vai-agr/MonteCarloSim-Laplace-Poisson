import random_walk as rw     #imported random_walk.py for using the randomWalk1D function
import matplotlib.pyplot as plt  #for graphing functions

number_of_walks = 400		 #Number of random walks for each point
step_size = 1				 #Distance between each point = 1cm i.e. 10 divisions
length = 10					 #Distance between the plates of the capacitor= 10cm	
boundary_voltages = [0,5]    #Voltages of the two plates of the capacitor in Volts
epsilon_o = 8.85e-12		 #Permittivity of free space
rho = 1e-14		 			 #Charge density in C/m^3	

if __name__ == "__main__":		#the main part

	f = -rho/epsilon_o			#RHS of the Poisson equation
	F = []						
	P_a = []
	points = [i for i in range(0,length+step_size,step_size)]
	for point in points:
		(ans,prob) = rw.randomWalk1D(number_of_walks,point,[0,length],step_size)  #length starts at 0
		#print(ans)
		P_a.append(prob)		#Probability of reaching boundary(whilst Random Walking) for all the points
		F.append(f*sum([len(i) for i in ans])*(step_size**2)*10e-4) #count number of points in each call to the randomWalk1D function
		#print(F)

	print(P_a)
	voltage_final = [(i*boundary_voltages[1]+ (1-i)*boundary_voltages[0])-j for i,j in zip(P_a,F)]  #calculated voltages at all points using Monte Carlo methods
	voltage_actual = [boundary_voltages[0]+(i/length)*(boundary_voltages[1]- boundary_voltages[0])-(i**2)*(0.5*rho/epsilon_o)*10e-4 for i in points]   #actual distribution of voltages across the points
	plt.plot(voltage_final, marker='o')
	plt.plot(voltage_actual)
	plt.show()