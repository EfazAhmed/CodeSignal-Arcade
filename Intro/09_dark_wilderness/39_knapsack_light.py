def solution(value1, weight1, value2, weight2, maxW):
    boo1 = weight1 <= maxW
    boo2 = weight2 <= maxW
    
    
    if boo1 and boo2:
        if weight1 + weight2 <= maxW:
            return value1 + value2
        return max(value1, value2)
    else:
        if boo1 and not boo2:
            return value1
        elif boo2 and not boo1:
            return value2
        else:
            return 0
