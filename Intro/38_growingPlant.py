import math

def solution(upSpeed, downSpeed, desiredHeight):
    
    day = 0
    curr = 0
    
    while True:
        day += 1
        curr += upSpeed
        if curr >= desiredHeight:
            return day
        curr -= downSpeed
        
    
