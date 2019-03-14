def solve(n):
    Ds = list(filter(lambda x: x**(1/2) % 1 != 0, [i for i in range(2, n)]))
    x_max = 0
    D_max_x = 0
    for D in Ds:
        print(D)
        x = diophant(D)
        if x > x_max:
            x_max = x
            D_max_x = D
    return x_max, D_max_x


def diophant(D): #finds minimal solutions for the formula x^2 + D*y^2 = 1
    y = 1
    while True:
        if (D * y**2 + 1)**(1 / 2) % 1 == 0: #test if the result gives a square number
            return int((D * y**2 + 1)**(1 / 2))
        y += 1

def phant(x, y):
    return x**2 + 2 * y**2, 2*x*y


"""
n = 1
while n < 10:
    if n == 1:
        x, y = phant(3, 2)
    else:
        x, y = phant(x, y)
    print(x, y)
    print(x/y)
    n += 1
    
"""