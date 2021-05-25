ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
tens = [6, 6, 5, 5, 5, 7, 6, 6]

def letter_count(n):
    result = 0
    u = str(n)
    while len(u) < 3:
        u = "0" + u
    hundred = int(u[0])
    ten = int(u[1])
    one = int(u[2])
    if hundred != 0:
        result += 7 + ones[hundred]
    if hundred != 0:
        result += 3
    if ten == 1:
        twi = int(str(ten) +  str(one))
        result += ones[twi]
    if ten !=1 and ten != 0:
        result += tens[ten - 2]
        result += ones[one]
    if ten == 0 and one != 0:
        result += ones[one]
    return result



def solve(n=1000):
    result = 0
    for i in range(1, n):
        result += letter_count(i)
    return result + 11
    
    

