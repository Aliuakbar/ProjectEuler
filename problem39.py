def solve():
	m = 0
	i = 0
	for p in range(1001):
		sols = []
		for a in range(p/3, p):
			for b in range((p-a)/2, p-a):
				c = p - a - b
				if a > b > c:
					if a*a == b*b + c*c:
						sols.append((a, b, c))
		if p == 840:
			print(sols)
		if m < len(sols):
			m = len(sols)
			i = p
	return m, i

print(solve())
