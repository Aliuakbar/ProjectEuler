def solve():
	result = []
	t = 1
	for x in range(10, 100):
		for y in range(10, 100):
			if x < y:
				if str(x)[0] == str(y)[1]:
					if x / float(y) == int(str(x)[1]) / float(str(y)[0]):
						result.append(x/float(y))
				elif str(x)[1] == str(y)[0] and str(y)[1] != "0":
					if x / float(y) == int(str(x)[0]) / float(str(y)[1]):
						result.append(x/float(y))
	for r in result:
		t *= r
	return t

print(solve())
#1/100 * 1/2
