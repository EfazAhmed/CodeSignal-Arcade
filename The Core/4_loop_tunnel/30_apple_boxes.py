def solution(k):
    red = 0
    yellow = 0
    for i in range(1, k+1):
        if pow(i, 2) % 2 != 0:
            red += pow(i, 2)
        else:
            yellow += pow(i, 2)
    return yellow - red
