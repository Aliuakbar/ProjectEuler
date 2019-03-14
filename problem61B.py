def triangluar_check(n):
	if n <= 0:
		return False
	if (8*n+1)**(1/2) % 1 == 0:
		return True
	return False

def square_check(n):
	if n <= 0:
		return False
	if n**(1/2) % 1 == 0:
		return True
	return False

def pentagonal_check(n):
	if n <= 0:
		return False
	if (24*n+1)**(1/2) % 6 == 5:
		return True
	return False

def hexagonal_check(n):
	if n <= 0:
		return False
	if ((8*n+1)**(1/2) + 1)/4 % 1 == 0:
		return True
	return False

def heptagonal_check(n):
	if n <= 0:
		return False
	if (3+(9+40*n)**(1/2))/10 % 1 == 0:
		return True
	return False

def octagonal_check(n):
	if n <= 0:
		return False
	if (1 + (1 + 3*n)**(1/2))/3 % 1 == 0:
		return True
	return False
 
