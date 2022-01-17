def solution(inputString):
    inputString = inputString.lower()
    middle = len(inputString)//2
    
    if len(inputString) % 2 == 0:
        first = inputString[:middle]
    else:
        first = inputString[:middle+1]
    
    second = inputString[middle:]

    return first == second[::-1]