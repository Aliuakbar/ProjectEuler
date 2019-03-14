from euler_kit import *
def phi(n):
    result = 1
    if is_prime(n) == True:
        return n - 1
    else:
        x = prime_factors(n)
        seen = []
        for i in x:
            if i in seen:
                result *= i
            else:
                result *= phi(i)
                seen.append(i)
        return result
    
def solve():
    i = 10**7
    result = [0, 10**10, 0]
    while i>1:
        if i % 100000 == 0:
            print("i")
        if is_permut(phi(i), i) == True:
            if i/phi(i) < result[1]:
                result = [i, i/phi(i), phi(i)]
                print(result)
        i -= 1
    return result
    
    
        
