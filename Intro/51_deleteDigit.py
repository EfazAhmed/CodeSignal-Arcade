import math

def solution(n):
    max_ = math.inf * -1
    
    li = [x for x in str(n)]
    
    for i in range(len(li)):
        value = li.pop(i)
        new = int("".join(li))
        if new > max_:
            max_ = new
        li.insert(i, value)
    
    return max_
        
