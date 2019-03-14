r = 1
n = 1001//2
x = 1
step = 0
for i in range(n):
    step += 2
    for i in range(4):
        r += x + step
        x += step
print(r)
        
