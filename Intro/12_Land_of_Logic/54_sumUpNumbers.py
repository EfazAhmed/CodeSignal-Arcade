def solution(inputString):
    
    temp = ""
    
    for i in range(len(inputString)):
        if inputString[i].isdigit():
            temp += inputString[i]
        else:
            temp += " "
    
    li = temp.split()
    
    curr = 0
    
    for el in li:
        if el.isdigit():
            curr += int(el)
            
    return curr
