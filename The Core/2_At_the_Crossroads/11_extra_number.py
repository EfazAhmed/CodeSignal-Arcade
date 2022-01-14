def solution(a, b, c):
    
    for letter in [a,b,c]:
        if [a,b,c].count(letter) == 1:
            return letter
        
