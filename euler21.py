def factors(n):
    result = []
    for i in range(1, n):
        if n % i == 0:
            result.append(i)
    return result

def amicable(n):
    firstsum = sum(factors(n))
    if n == sum(factors(firstsum)) and n != firstsum:
        return True
    else:
        return False
    
def find_amics(limit):
    result = 0
    for i in range(limit):
        if amicable(i) == True:
            print(i)
            result += i
    return result
