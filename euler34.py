import time
def isdf(n):
    fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    nums = list(str(n))
    result = 0
    if n == 1 or n == 2:
        return False
    for i in range(len(nums)):
        result += fact[int(nums[i])]
    if result == n:
        return True
    else:
        return False

def df2():
    result = 0
    start = time.time()
    for i in range(362880):
        if isdf(i) == True:
            result += i
            print(i)
    end = time.time()
    print(end - start)
    return result

        
        
	
	
