from functools import reduce
from operator import mul
"""corrupted"""

def isprime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
  
def primes_to_n(n):
	primes = {2}
	j = 3
	while j <= n:
		if isprime(j):
			primes.add(j)
		j += 2
	return primes

def unique_prime_factors(n):
    assert(n >= 2)
    prime_factors = set()
    while not isprime(n):
        i = 2
        while i*i <= n:
            if n % i == 0:
                prime_factors.add(int(i))
                n /= i
            i += 1
    prime_factors.add(int(n))
    return prime_factors


def func(a=5):
    n = 1
    while n <= 3*a:
        r = ((a - 1)**n + (a + 1)**n) % a**2
        print(f"{n}->{r}") 
        n += 1

def test():
    assert(primes_to_n(11) == {2, 3, 5, 7, 11})
    assert(unique_prime_factors(12) == {2, 3})
    assert(unique_prime_factors(7) == {7})
    assert(max_remainder(7) == 42)
    assert(max_remainder(11) == 110)
    print("tests succesfull")

def max_remainder(a):
    r_max = 0
    if isprime(a):
        p = 2*a + 1
    else:
        p = reduce(mul, unique_prime_factors(a)) + 1
    for n in range(p):
        r = ((a - 1)**n + (a + 1)**n) % a**2
        if r > r_max:
            r_max = r
    return r_max

def solve():
    r_sum = 0
    for a in range(3, 1001):
        print(a)
        r_sum += max_remainder(a)
    return r_sum

if __name__ == "__main__":
    test()
    print(solve())
   
         