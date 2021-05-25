import math


def fact(n):
    assert isinstance(n, int)
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * fact(n - 1)


def choose(n, p):
    return fact(n) / (fact(n - p) * fact(p))


def test():
    assert fact(5) == 120
    assert choose(5, 3) == 10


def helper(n):
    for i in range(n + 1):
        print(f"{i} -> {choose(n, i)%7}")


def proto_solve():
    """ first 100 rows """
    m = math.floor(100 / 7)

    return m * (m + 1) / 2 * 28


def triangle(n):
    with open("pascal.txt", "w") as file:
        result = 0
        for i in range(n):
            seq = ""
            for j in range(i + 1):
                if choose(i, j) % 7 == 0:
                    seq += "° "

                else:
                    seq += "# "
                    result += 1
            file.write(" " * (n - i - 1) + seq + " " * (n - i - 1) + "\n")
        return result


if __name__ == "__main__":
    test()
    print(triangle(98))
    # for i in range(28, 35):
    #     print(i)
    #     helper(i)
# print(proto_solve())
