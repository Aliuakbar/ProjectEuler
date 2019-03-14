def main():
    """
    matrix = [[131, 673, 234, 103, 18],
              [201, 96 ,342, 965, 150],
              [630, 803, 746, 422, 111],
              [537, 699, 497, 121, 956],
              [805, 732, 524, 37, 331]]
    return solve(matrix)
    """

    with open("p081_matrix.txt", "r") as file:
        content = file.readlines()
        matrix = []
        for line in content:
            matrix.append(line.strip("\n").split(","))
        for index, line in enumerate(matrix):
            matrix[index] = [int(e) for e in line]
        return solve(matrix)


def solve(matrix):
    n = len(matrix)
    for i in range(1, n):
        x = i
        y = 0
        while x >= 0:
            if y == 0:
                matrix[y][x] += matrix[y][x - 1]
            elif x == 0:
                matrix[y][x] += matrix[y - 1][x]
            else:
                matrix[y][x] += min(matrix[y][x - 1], matrix[y - 1][x])
            x -= 1
            y += 1

    for i in range(1, n):
        x = n - 1
        y = i
        while y != n:
            if y == 0:
                matrix[y][x] += matrix[y][x - 1]
            elif x == 0:
                matrix[y][x] += matrix[y - 1][x]
            else:
                matrix[y][x] += min(matrix[y][x - 1], matrix[y - 1][x])
            y += 1
            x -= 1
    for line in matrix:
        print(line)
    return matrix[n - 1][n - 1]


if __name__ == '__main__':
    print(main())

"""
for x in range(1, n):
        for y in range(x):
            if y - 1 < 0:
                matrix[y][x - y] += matrix[y][x - y - 1]
            elif x - y - 1 < 0:
                matrix[y][x - y] += matrix[y - 1][x - y]
            else:
                matrix[y][x - y] += min(matrix[y - 1][x - y], matrix[y][x - y - 1])
"""
