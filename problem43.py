def fact(n):
	if n == 1:
		return 1
	else:
		return n*fact(n-1)

#fact(10) 0-10 pandidigtal numbers

from itertools import permutations

permuts = list(permutations("0123456789"))
print("Permutated")
perm = []
for p in permuts:
	temp = ""
	for i in p:
		temp += i
	perm.append(temp)


sols = []
for p in perm:
	if p[0] == "0":
		continue
	if int(p[7:10]) % 17 != 0:
		continue
	if int(p[6:9]) % 13 != 0:
		continue
	if int(p[5:8]) % 11 != 0:
		continue
	if int(p[4:7]) % 7 != 0:
		continue 
	if int(p[3:6]) % 5 != 0:
		continue
	if int(p[2:5]) % 3 != 0:
		continue
	if int(p[1:4]) % 2 == 0:
		sols.append(int(p))

print(sols)
print(sum(sols))
