def solution(inputString):

    length = len(inputString)
    idx = int(length / 2)
    
    if length % 2 != 0:
        first = inputString[0:idx+1]
        second = inputString[idx:][::-1]
        return first == second
    else:
        first = inputString[0:idx]
        second = inputString[idx:][::-1]
        return first == second