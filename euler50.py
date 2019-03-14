import primes as pr
l = 100
res = []
ss = [s for s in pr.tonprime(l)]
for s in ss:
    primesum = 0
    for i in range(len(ss)):
        if len(ss) > (i + s):
            primesum += ss[s + i]
            if pr.is_prime(primesum) == True and primesum < l:
                res.append(primesum)
print(res)
    
    



    
