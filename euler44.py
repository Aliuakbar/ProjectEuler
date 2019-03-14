from math import sqrt
import time
start = time.time()

def pent(n):
    return int(n * (3*n -1) / 2)

def ispent(n):
    if n == 0:
        return True
    elif ((sqrt(24 * n + 1 if n > 0 else 1) + 1) / 6) % 1 == 0:
        return True
    else:
        return False

rang = 3000

result = []

for i in range(1, rang):
    tempi = pent(i)
    for y in range(1, rang):
        tempy = pent(y)
        if y == i:
            continue
        if ispent(tempi + tempy) and ispent(tempi - tempy):
            result.append((abs(tempi - tempy), (tempi, tempy)))
end = time.time()
print(result)
print("It took {0} seconds".format(round((end - start), 2)))


                

