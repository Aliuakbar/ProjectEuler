import primes
import itertools

def create_list(a, b):
    ls = []
    for i in range(a, b+1):
        ls.append(ad_fact(i))
    return ls

def ad_fact(n):
    factors = primes.prime_factors(n)
    new = []
    did = []
    for factor in factors:
        if factor not in did:
            new.append([factor, factors.count(factor)])
            did.append(factor)
    for i in range(len(new)):
        if new[i][1] % 2 == 0:
            new[i][1] = True
        else:
            new[i][1] = False
    return new
	
def flatten(seq,container=None):
    if container is None:
        container = []
    for s in seq:
        if hasattr(s,'__iter__'):
            flatten(s,container)
        else:
            container.append(s)
    return container

def combs(it):
    return list(itertools.combinations(it, 2))

def validate(comb):
    comb = flatten(comb)
    nums = list(set([x for x in comb if type(x) == type(3)]))
    return nums
    

    
