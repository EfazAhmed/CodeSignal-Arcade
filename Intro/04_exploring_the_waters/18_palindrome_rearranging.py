def solution(inputString):
    s = {}
    
    for letter in inputString:
        if not letter in s.keys():
            s[letter] = 1
        else:
            s[letter] += 1
            
    count = 0
    
    for key in s.keys():
        if s[key] % 2 != 0:
            count += 1
            
    return count <= 1
        
        

