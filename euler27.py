#solved
import math
def is_prime(n):
    if n < 0:
        return False
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def euler27():
    nm = 0
    tm = 0
    for a in range(-1000, 1000):
        for b in range(-1000, 1000):
            n = 0
            while True:
                if is_prime(n ** 2 + a * n + b) == True:
                    n += 1
                else:
                    if n >= nm:
                        nm = n
                        tm = (a, b)
                    break
    return(n, tm)

def iterate(a, b):
    n = 0
    i = 0
    while True:
        value = i**2 + a*i + b
        if is_prime(value) == True:
            n += 1
            i += 1
        else:
            break
    return n

