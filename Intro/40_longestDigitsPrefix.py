def solution(inputString):
    temp = ""
    
    for letter in inputString:
        if letter.isdigit():
            temp += letter
        else:
            break
        
    return temp