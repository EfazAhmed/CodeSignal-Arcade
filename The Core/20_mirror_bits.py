def solution(a):
    binary = bin(a)[2:]
    rev = binary[::-1]
    return int(rev, 2)