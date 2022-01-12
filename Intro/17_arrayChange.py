def solution(inputArray):
    if len(list(set(inputArray))) == 1:
        return len(inputArray)
        
    count = 0
    
    for i in range(len(inputArray)-1):
        if inputArray[i] >= inputArray[i+1]:
            addition = inputArray[i] - inputArray[i+1] + 1
            count += addition
            inputArray[i+1] += addition
        
    return count


 