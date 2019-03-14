def collatz(n):
    if n % 2 == 0:
        return n//2
    return 3 * n + 1

def sequence(n):
    steps = 1
    while True:
        if n == 1:
            return steps
        n = collatz(n)
        steps += 1

def solve(n=1000000):
    longest = [0, 0]
    for i in range(2, n):
        if sequence(i) > longest[0]:
            longest[0] = sequence(i)
            longest[1] = i
    return longest

def print_collatz(n):
    while True:
        if n == 1:
            print(1)
            break
        print(n)
        n = collatz(n)
