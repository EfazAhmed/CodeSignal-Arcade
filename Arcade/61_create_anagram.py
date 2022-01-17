def solution(s, t):
    a = getFrequencies(s)
    b = getFrequencies(t)
    
    difference = getDifferences(s, b)
    return difference

def getFrequencies(s):
    dic = {}
    for letter in s:
        if letter not in dic.keys():
            dic[letter] = 1
            continue
        dic[letter] += 1
    return dic
        
def getDifferences(s, b):
    count = 0
    for letter in s:
        if letter not in b.keys():
            count += 1
        elif b[letter] > 0:
            b[letter] -= 1
        else:
            count += 1
    return count
