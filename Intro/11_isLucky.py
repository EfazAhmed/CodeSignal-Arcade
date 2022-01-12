def solution(n):
    s = str(n)
    length = len(s)
    first = s[0:int(length/2)]
    second = s[int(length/2):]
    
    return sum([int(i) for i in first]) == sum([int(i) for i in second])