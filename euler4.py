def is_palindrom(x):
    if x == int(str(x)[::-1]):
        return True
    else:
        return False
result = 0
i = 999
while i > 100:
    y = 999
    while y > i:
        prod = i * y
        if prod <= result:
            break
        if is_palindrom(prod) == True and prod > result:
            result = prod
        y -= 1
    i -= 1
print(result)
