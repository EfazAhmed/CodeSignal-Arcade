def solution(a, b):
    
    if a == b:
        return 1
    
    freq = {}
    
    for letter in b:
        if letter not in freq.keys():
            freq[letter] = 1
        else:
            freq[letter] += 1
            
    words = 0
            
    while True:
        found = True
        print(freq)
        for letter in a:
            if letter in freq.keys():
                if freq[letter] > 0:
                    freq[letter] -= 1
                else:
                    return words
            else:
                return words
        if found:
            words += 1
                
    return words