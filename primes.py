import math
import itertools

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def nprimes(n):
	x = []
	j = 2
	while len(x) < n:
		if is_prime(j) == True:
			x.append(j)
		j += 1
	return x
    
def primes_to_n(n):
    x = [2]
    j = 3
    while x[-1] < n:
	    if is_prime(j) == True:
	    	x.append(j)
	    j += 1
    return x

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
    
def divisors(n):
    factors = prime_factors(n)
    divisors = []
    for i in range(1, len(factors) + 1):
        x = list(itertools.combinations(factors, i))
        for y in range(len(x)):
            divisors.append(x[y])
    divisors = list(set(divisors))
    return len(divisors)
            
    

