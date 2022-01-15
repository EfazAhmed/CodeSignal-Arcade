def solution(n):
    rev = str(n)[::-1]
    first = -1
    
    for i, letter in enumerate(rev):
        if letter != "0":
            first = i
            rev = rev[first+1:]
            break
        
    if first == -1:
        return False
    
    second = -1
    for i, letter in enumerate(rev):
        if letter == "0":
            second = i
            break
    if second == -1:
        return False
    else:
        return True
