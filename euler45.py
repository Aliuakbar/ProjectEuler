def triagonal(n):
    return int(n * (n + 1) / 2)

def pentagonal(n):
    return int(n * (3 * n - 1) / 2)

def hexagonal(n):
    return int(n * (2 * n - 1))

i = 286
while True:
    for y in range(i):
        if triagonal(i) == pentagonal(y):
            for z in range(y):
                if triagonal(i) == hexagonal(i):
                    print(i)
                    break
        else:
            i += 1
    else:
        i += 1
