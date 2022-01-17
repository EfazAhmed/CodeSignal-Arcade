def solution(n):
    sequence = step(n)
    
    key = 0
    count = 0
    
    for num in list(set(sequence)):
        if sequence.count(num) > count:
            count = sequence.count(num)
            key = num
        elif sequence.count(num) == count:
            if num > key:
                key = num
    
    return key            
    
def step(x):
    if x == 0:
        return [0]
    else:
        total = getSum(x)
        return [total] + step(x-total)
    
    
def getSum(s):
    s = str(s)
    return sum([int(x) for x in s])