def solution(cell1, cell2):
    l_1 = ord(cell1[0]) % 2 == 0
    l_2 = ord(cell2[0]) % 2 == 0
    n_1 = int(cell1[1]) % 2 == 0
    n_2 = int(cell2[1]) % 2 == 0

    return getColor(l_1, n_1) == getColor(l_2, n_2)
    
    
    
def getColor(l, n):
    if not l and not n:
        return "b"
    elif l and not n:
        return "w"
    elif not l and n:
        return "w"
    else:
        return "b"