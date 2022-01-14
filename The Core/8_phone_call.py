def solution(min1, min2_10, min11, s):
    
    curr = 1
    
    while True:
        if curr == 1:
            if s >= min1:
                s -= min1
                curr += 1
            else:
                return curr-1
        elif curr >= 2 and curr <= 10:
            if s >= min2_10:
                s -= min2_10
                curr += 1
            else:
                return curr-1
        elif curr > 10:
            if s >= min11:
                s -= min11
                curr += 1
            else:
                return curr-1
        else:
            return curr-1
    
    
