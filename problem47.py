import math

def quad_factor(n):
	i = 2
	factors = []
	n_start = n
	while i * i < n_start:
		if n % i == 0:
			temp_i = 0
			while n % i == 0:
				n /= i
				temp_i += 1
			factors.append(i**temp_i)

			if len(factors) > 4:
				return False

		i += 1
	return factors

def solve():
	n = 2*3*5*7
	distinct = []
	counter = 0
	while couter < 4:
		
		n+=1


print(quad_factor(644))