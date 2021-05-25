import primes

def seq(k, n):
    i = 3
    c = 0
    x = 1 + k ** 2
    while c < n:
        yield x
        x += i
        i += 2
        c += 1

def debug():
    y = 3
    for i, x in enumerate(seq(3, 20)):
        p = primes.prime_factors(x)
        print(f"{i+1}   {x}   {' '.join(map(str, p))}   {y}   {y in p}")
        y += 2

def debug2(k):
    c = 1
    i = 3
    x = 1 + k ** 2
    while True:
        p = primes.prime_factors(x)
        if i in p:
            print(f"{c}   {x}   {' '.join(map(str, p))}   {i}   {i in p}")
        x += i
        i += 2
        c += 1

def helper(k):
    c = 1
    i = 3
    x = 1 + k ** 2
    while True:
        p = primes.prime_factors(x)
        if i in p:
            return i
        x += i
        i += 2
        c += 1

def prime_gen():
    yield 2
    yield 3
    y = 3
    i = 2
    while True:
        y += 2
        i = 2
        prime = True
        while i * i <= y:
            if y % i == 0:
                prime = False
                break
            i += 1
        if prime: yield y

def modified_prime_gen():
    yield (1, 3)
    y = 3
    i = 2
    s = 1
    while True:
        y += 2
        i = 2
        prime = True
        while i * i <= y:
            if y % i == 0:
                prime = False
                s += 1
                break
            i += 1
        if prime:
            yield (s, y)
            s = 1

def new_helper(k):
    i = 3
    x = 1 + k ** 2
    gen = modified_prime_gen()
    s, p = next(gen)
    while True:
        if x % p == 0:
            return p
        s, p = next(gen)
        for _ in range(s):
            x += i
            i += 2


if __name__ == '__main__':
    gen = modified_prime_gen()
    i = 1
    while True:
        print(new_helper(i))
        i += 1