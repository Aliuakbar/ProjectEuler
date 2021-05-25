import itertools

def generate(n):
    """number generator, works iterative. Returns n numbers"""
    numbers = [290797]
    i = 0
    while i < 2 * n - 1:
        numbers.append((numbers[i] ** 2) % 50515093)
        i += 1
    return numbers

def points(n):
    """uses generate to create points. Returns a list of n points
        a point consists of a tuple with the x and y coordinate"""
    points = []
    numbers = generate(n + 1)
    for i in range(1, n + 1):
        points.append(((numbers[2 * i - 1] % 2000) -1000,
                     (numbers[2 * i]% 2000)-1000))
    return points

def lines(n):
    """combinates all points to create lines"""
    return list(itertools.combinations(points(n), 2))

def line(paircoord):
    """line based on two points, returns the slope and a = f(0)"""
    x0 = paircoord[0][0]
    y0 = paircoord[0][1]
    x1 = paircoord[1][0]
    y1 = paircoord[1][1]
    dx = x1 - x0
    dy = y1 - y0
    if dx == 0:
        return(0, dy)
    else:
        slope = dy / dx
    a = y0 - x0 * slope
    return (slope, a)

def funcs():
    return len(set(func))

def parallels():
    """parallels have same slope"""
    ocs = []
    f = 0
    n = len(func)

    while f < n-1:
        i = 1
        while f + i < n:
            if func[f][0] == func[f+i][0]:
                i += 1
                if f + i == n -1:
                    ocs.append(i-1)
                    f += i
                    break
            else:
                if i != 1:
                    ocs.append(i-1)
                f += i
                break
##    ocs.remove(max(ocs))
##    ocs = list(map(lambda x: sl(x+1), ocs))
    return ocs
            
def sl(n):
    return n * (n-1)

def solve():
    return sl(funcs()) - len(parallels())

lins = lines(100)
func = [line(i) for i in lins]
func.sort()

##if __name__ == "__main__":
##    result = solve(2500)
##    print(result)
    
        
