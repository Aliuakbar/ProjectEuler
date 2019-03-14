import primes
from itertools import combinations

factors = [3, 3, 5, 5, 7, 11, 13, 31, 41, 61, 151, 331, 1321]

def mult(tup):
    if len(tup) == 0:
        return 1
    result = 1
    for i in range(len(tup)):
        result *= tup[i]
    return result + 1

def solve():
    result = 0
    factors = primes.prime_factors(2**60 -1)
    lo = []       
    for i in range(1, len(factors) + 1):
        li = list(combinations(factors, i))
        lo.append(li)
    for i in range(len(lo)):
        for y in range(len(lo[i])):
            if (61 in lo[i][y]) or (1321 in lo[i][y]):
                result += mult(lo[i][y])
    print(result)

def test():
    result = 0
    factors = primes.prime_factors(2**10 -1)
    lo = []       
    for i in range(1, len(factors) + 1):
        li = list(combinations(factors, i))
        lo.append(li)
    for i in range(len(lo)):
        for y in range(len(lo[i])):
            if (11 in lo[i][y]):
                result += mult(lo[i][y])
    return result

def shuffle(stack):
    h1 = stack[:len(stack)//2]
    h2 = stack[len(stack)//2:]
    new = []
    for i in range(len(stack)//2):
        new.append(h1[i])
        new.append(h2[i])
    return new

def multi_shuff(stack, n):
    i = n
    while i >= 1:
        stack = shuffle(stack)
        i -= 1
    return stack

def make_stack(n):
    stack = [i for i in range(1, n + 1)]
    return stack

def factor_list(n):
    factors = []
    for i in range(n):
        for prime in primes.prime_factors(2**i - 1):
            if prime not in factors:
                factors.append(prime)
    return factors

def uniques(n):
    facts = primes.prime_factors(2**n -1)
    factors = factor_list(n-1)
    unique = []
    for prime in facts:
        if prime not in factors:
            unique.append(prime)
    return unique
        


if __name__ == "__main__":
    solve()
