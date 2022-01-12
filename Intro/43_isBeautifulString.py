def solution(inputString):
    li = sorted([x for x in inputString])
    freq = {}
    
    alpha = "abcdefghijklmnopqrstuvwxyz"
    

    for letter in alpha:
        if letter in li:
            count = li.count(letter)
            freq[letter] = count          
        else:
            freq[letter] = 0
            
            
    values = list(freq.values())
    return values == sorted(values, reverse=True)
