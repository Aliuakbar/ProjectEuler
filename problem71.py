import fractions

def solve():
	nom = 2
	den = 2
	m = 100000
	s = nom, den
	while den < 1000000:
		if nom / den < 3/7:
			nom += 1
		else:
			den += 1
		if nom/den < 3/7: 
			if 3/7 - nom/den < m:
				m = 3/7 - nom/den
				s = nom, den
	print(m, s)
	f = fractions.Fraction(s[0], s[1])
	print(f)



solve()