import itertools
import math
import time

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def erat2( ):
    D = {  }
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p

def get_primes_erat(n):
  return list(itertools.takewhile(lambda p: p<n, erat2()))

def goldbach():
        start = time.time()
        i = 9
        primes = get_primes_erat(10000)
        while True:
                if is_prime(i) == False:
                        sub = False
                        for prime in primes[:i]:
                                if sub == True:
                                        break
                                for z in range(int(math.sqrt(i/2))+1):
                                        if i == prime + 2*(z**2):
                                                sub = True
                                                break
                        if sub == False:
                                end = time.time()
                                print("Solution {} found in {} seconds".format(i,round(end - start, 3)))
                                return i

                        
                i += 2
if __name__ == "__main__":
        goldbach()
