def coprime(n, m):
	facs = []
	i = 2
	nn = n
	while i <= n:
		if nn % i == 0:
			facs.append(i)
			nn /= i
		i += 1
	for f in facs:
		if m % f == 0:
			return False
	return True

def solve(n):
	c = 0
	for i in range(1, n + 1):
		for y in range(i + 1, n + 1):
			if coprime(i, y):
				c += 1
	return c

print(solve(1000))
