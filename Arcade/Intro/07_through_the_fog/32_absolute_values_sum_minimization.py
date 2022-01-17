import math

def solution(a):
    diff = math.inf
    curr = a[0]
    
    for i in range(len(a)):  
        temp = 0
        for j in range(len(a)):
            temp += abs(a[j] - a[i])
        if temp < diff:
            curr = a[i]
            diff = temp
    
    return curr
    
    
