def solution(inputString):
    if len(inputString) % 2 == 1:
        return False
    first = inputString[:len(inputString)//2]    
    second = inputString[len(inputString)//2:] 
    return first == second
