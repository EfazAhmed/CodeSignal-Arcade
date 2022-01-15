def solution(st):
    
    if st == st[::-1]:
        return st
    
    length = 1
    
    while True:
        if length <= len(st):
            addition = st[:length]
            rev = addition[::-1]
            new = st + rev
            if new == new[::-1]:
                return new
        length += 1
            
        
