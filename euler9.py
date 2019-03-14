c, b, a = 997, 2, 1
while c > b:
    a = 1
    b = 2
    if c % 50 == 0:
            print(c)
    while a < b and a < c:
        b = 1000 - a - c
        if a**2 + b**2 == c**2:
            print(a*b*c)
            print(a, b, c)
        a += 1
    c -= 1
