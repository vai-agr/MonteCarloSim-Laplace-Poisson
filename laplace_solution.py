import random_walk as rw


if __name__ == "__main__":

	ans = rw.randomWalk1D(100,5,10,[0,10],1)
	for i in ans:
		print(i)