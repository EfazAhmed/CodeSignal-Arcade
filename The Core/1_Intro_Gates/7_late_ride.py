def solution(n):
    hours = n % 60
    n = int(n / 60)
    minutes = n
    
    time = str(hours) + str(minutes)
    
    return sum([int(i) for i in time])
