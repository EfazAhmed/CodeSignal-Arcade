import math

def solution(a, b):
    count = 0
    for i in range(-(a+100), a+111):
        for j in range(-(b+100), b+111):
            x = (i+j)/math.sqrt(2)
            y = (j-i)/math.sqrt(2)
            
            if x < a/2 and x > -a/2:
                if y < b/2 and y > -b/2:
                    count += 1
    return count
