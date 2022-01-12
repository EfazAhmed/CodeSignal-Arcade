import math

def solution(inputArray):
    temp = -1 * math.inf
    for i in range(len(inputArray)-1):
        prod = inputArray[i] * inputArray[i+1]
        if prod > temp:
            temp = prod
    return temp
        