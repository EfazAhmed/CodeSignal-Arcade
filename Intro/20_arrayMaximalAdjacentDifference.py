def solution(inputArray):
    max = 0
    for i in range(len(inputArray)-1):
        if abs(inputArray[i]-inputArray[i+1]) > max:
            max = abs(inputArray[i]-inputArray[i+1])
    return max
