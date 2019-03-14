def is_prime(n):
	if n <= 1:
		return False
	i = 2
	while i*i <= n:
		if n % i == 0:
			return False
		i += 1
	return True

def solve(limit):
	p = 2
	m = 0
	n = 0
	Primes = []
	while True:
		while sum(primes) < limit:
			primes.append(p)
			print(len(primes), primes, sum(primes))
			last = p
			if is_prime(sum(primes)) and sum(primes) < limit:
				m = sum(primes)
				print(m)
			p += 1
			while not is_prime(p):
				p += 1
		if sum(primes) > limit:
			del primes[-1]
			p = primes[-1] + 1
			while not is_prime(p):
				p += 1	
		if len(primes) > 2:
			del primes[0]
		else:
			break
		
	return m


print(solve(1000))