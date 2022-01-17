def solution(inputString):
    numbers = "0123456789"
    letters = "ABCDEF"
    
    li = inputString.split("-")
    
    if len(li) != 6:
        return False
        
    for part in li:
        if len(part) != 2:
            return False
        else:
            for char in part:
                if char not in numbers and char not in letters:
                    return False
    
    return True
