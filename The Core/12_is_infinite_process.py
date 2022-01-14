def solution(a, b):
    diff = b - a
    if diff < 0:
        return True
    if diff % 2 == 1:
        return True
    else:   
        return False

