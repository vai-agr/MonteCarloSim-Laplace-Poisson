import random_walk as rw


if __name__ == "__main__":

	P_a =[]
	for i in range(1,10,1):

		(ans,prob) = rw.randomWalk1D(10,i,10,[0,10],1)
		#print(ans)
		P_a.append(prob)
	print(P_a)	
		


