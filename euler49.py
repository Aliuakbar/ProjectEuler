"""
solved 29.8.18
"""
from euler_kit import get_primes_erat
from itertools import combinations
p = get_primes_erat(10000)[168::]

def is_permut(x, y):
    x = [int(i) for i in str(x)]
    y = [int(i) for i in str(y)]
    for digit in x:
        if digit not in y:
            return False
        y.remove(digit)
    return True

def find_permut():
    p = get_primes_erat(10000)[168::]
    result = []
    for prime in p:
        p.remove(prime)
        temp = []
        for other_prime in p:
            if is_permut(prime, other_prime) == True:
                p.remove(other_prime)
                if temp == []:
                    temp.append(prime)
                    temp.append(other_prime)
                else:
                    temp.append(other_prime)
        result.append(temp)
    for r in result:
        r = r.sort()
    return result

def three_permut():
    permuts = find_permut()
    pf = []
    for p in permuts:
        if len(p) == 3:
            pf.append(p)
        if len(p) > 3:
            combi = list(combinations(p, 3))
            for c in combi:
                pf.append(c)
    
    return pf

def is_arithemtic(n):
    if n[2] - n[1] == n[1] - n[0]:
        return True
    return False

def solve():
    result = []
    permuts = three_permut()
    for t in permuts:
        if is_arithemtic(t) == True:
            result.append(t)
    return result
        
    
    
    

            
    
