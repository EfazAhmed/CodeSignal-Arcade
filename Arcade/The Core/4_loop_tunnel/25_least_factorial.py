def solution(n):
    curr = 1
    while True:
        value = factorial(curr)
        if value >= n:
            return value
        curr += 1
        
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
        