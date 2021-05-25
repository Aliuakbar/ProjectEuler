import time
def isprime(n):
	if n < 2:
		return False
	for i in range(2 ,n):
		if n % i == 0:
			return False
			break
	else:
		return True

def nthprime(n):
	start = time.time()
	x = []
	j = 2
	while len(x) < n:
		if isprime(j) == True:
			x.append(j)
		j += 1
	print("The solution is: {0}".format(x[n-1]))
	end = time.time()
	passed = end - start
	print("It took me {0} seconds to solve this exercise".format("%.2f" % passed))

	
