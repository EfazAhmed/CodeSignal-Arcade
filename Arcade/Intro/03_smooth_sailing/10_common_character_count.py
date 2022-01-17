def solution(s1, s2):
    dict1 = {}
    dict2 = {}
    
    for letter in s1:
        try:
            dict1[letter] += 1
        except KeyError:
            dict1[letter] = 1
            
    for letter in s2:
        try:
            dict2[letter] += 1
        except KeyError:
            dict2[letter] = 1
            
    count = 0           

    for letter in dict1.keys():
        if letter in dict2.keys():
            count += min(dict1[letter], dict2[letter])
    
    return count