def solution(s):
    lower = pow(10, len(s)-1)
    higher = pow(10, len(s))
    
    value = getIdenticals(s)
    
    s = "".join(sorted([x for x in s]))
    
    for i in range(higher, lower-1, -1):
        if pow(i, 1/2) == int(pow(i, 1/2)):
            if value == getIdenticals(i):
                return i
    return -1
        
        
def getIdenticals(s):
    dic = {}
    s = str(s)
    for letter in s:
        if letter not in dic.keys():
            dic[letter] = 1
            continue
        dic[letter] += 1
    return sorted(list(dic.values()))