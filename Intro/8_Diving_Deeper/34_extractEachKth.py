def solution(inputArray, k):
    temp = []
    for i in range(len(inputArray)):
        selection = i + 1
        if selection % k != 0:
            value = inputArray[i]
            temp.append(value)
            
    return temp
        
            
