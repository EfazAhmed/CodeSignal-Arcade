def solution(n, firstNumber):
    dist = int(n // 2)
    if firstNumber > dist:
        return abs(firstNumber - dist)
    elif firstNumber < dist:
        return firstNumber + dist
    else:
        return 0 
    
