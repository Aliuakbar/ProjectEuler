import primes

def next_triangular(tri, n):
    return tri + n + 1

def solve():
    tri = 1
    n = 1
    while True:
        tri = next_triangular(tri, n)
        if primes.divisors(tri) > 500:
            print(tri)
            break
        n += 1
