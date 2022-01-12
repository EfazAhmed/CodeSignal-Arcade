def solution(n):
    return all([int(x) % 2 == 0 for x in str(n)])
