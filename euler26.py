


result = []
for p in range(3, 1000):
    fraction = str(1 / p)
    for q in range(3, 10):
        for i in range(q + 1, len(fraction)):
            pattern = fraction[q:i]
            if 2 * pattern in fraction:
                result.append((p, i - 2))
                break
    
temp = [tup[1] for tup in result]
for i in range(len(result)):
    tup = result[i]
    if max(temp) in tup:
        print(tup)
    
