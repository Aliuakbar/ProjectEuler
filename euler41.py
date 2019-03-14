def pandigital(n):
    n = str(n)
    known = []
    for digit in n:
        if digit in known or digit == "0" or int(digit) > len(n):
            return False
        known.append(digit)
    return True

def is_prime(n):
    i = 2
    if n <= 1:
        return False
    while i <= n**(1/2):
        if n % i == 0:
            return False
        i += 1
    return True

def solve():
    n = 987654321
    while n > 2143:
        if n % 100000 == 0:
            print(n)
        if pandigital(n):
            if is_prime(n):
                return n
        n -= 2

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]

print(primes2(10**6))

