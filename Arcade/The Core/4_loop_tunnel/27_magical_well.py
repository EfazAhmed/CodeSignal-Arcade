def solution(a, b, n):
    current = 0
    while n > 0:
        current += (a*b)
        a += 1
        b += 1
        n -= 1
    return current
        
