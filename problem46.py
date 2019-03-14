from math import sqrt

def isprime(n):
	if n < 2:
		return False
	for i in range(2 ,n):
		if n % i == 0:
			return False
	else:
		return True

    
def primes(n):
	x = []
	j = 2
	while len(x) < n:
		if isprime(j) == True:
			x.append(j)
		j += 1
	return x
def goldbach():
    n = 9
    while True:
        for prime in primes(n):
            for i in range(int(sqrt(n))):
                if i == int(sqrt(n)):
                    return n
                    break
                else:
                        continue

        print(n)
                
        n += 2

def goldbach2(n):
        for i in range(9, n , 2):
                goldbach = False
                if isprime(i) == True:
                        continue
                for num in range(int(sqrt(i))):
                        squared = 2 * num * num
                        if goldbach == True:
                                        continue
                        for prime in primes(i):
                                if squared + prime == i:
                                        print("2 * {0} * {0} + {1} = {2}".format(num, prime, i)) 
                                        goldbach = True
                                        
                if goldbach == False:
                        print("for {0} the goldbach conjecture is false!".format(i))
	

def goldbach3():
        i = 9
        q = 0
        while True:
                goldbach = False
                if isprime(i) == True:
                        i += 2
                        continue
                if i > 100:
                        q = 50
                if i > 500:
                        q = 100
                if i > 1000:
                        q = 500
                for num in range(int(sqrt(i))):
                        squared = 2 * num * num
                        for prime in primes(i - squared - q):
                                if squared + prime == i:
                                        print("2 * {0} * {0} + {1} = {2}".format(num, prime, i)) 
                                        goldbach = True
                                        i += 2
                if goldbach == False:
                        print("for {0} the goldbach conjecture is false!".format(i))
                        break

                
