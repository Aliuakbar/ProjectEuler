from math import sqrt
def fib(n):
    return int(1 / sqrt(5) * (((1 + sqrt(5)) / 2 ) ** n
                              - ((1 - sqrt(5)) / 2) ** n))

result = 0
i = 3
while fib(i) < 4000000:
    result += fib(i)
    i += 3
print(result)
