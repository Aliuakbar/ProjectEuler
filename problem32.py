def solve():
	products = []
	for i in range(12345):
		if soft_check(i):
			for j in range(1, i/2 + 1):
				if i % j != 0:
					continue
				if not soft_check(j):
					continue
				m = i / j
				known = [digit for digit in str(i)]
				known.extend(str(j) + str(m))
				if len(known) < 9:
					continue
				if not soft_check2(known):
					continue
				if not final_check(known):
					continue
				products.append((i, j, m))
	return products

def final_check(n):
	for digit in n:
		if int(digit) not in range(1, len(n)+1):
			return False
	return True


def soft_check(n):
	known = []
	for digit in str(n):
		if digit in known:
			return False
		if digit == "0":
			return False
		known.append(digit)
	return True

def soft_check2(n):
	known = []
	for digit in n:
		if digit in known:
			return False
		if digit == "0":
			return False
		known.append(digit)
	return True

if __name__ == '__main__':
	print(solve())



