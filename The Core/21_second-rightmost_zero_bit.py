def solution(n):
    return pow(2, bin(n)[2:][::-1].find("0", bin(n)[2:][::-1].find("0")+1))
