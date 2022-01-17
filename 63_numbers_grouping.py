def solution(a):
    dic = {}
    
    for num in a:
        if num > pow(10, 6) and num < 1:
            continue
        else:
            if num % pow(10, 4) == 0:
                group = num // pow(10, 4) 
                group -= 1
            else:
                group = num // pow(10, 4)
            if group not in dic.keys():
                dic[group] = 1
                continue
            dic[group] += 1
            
    return len(list(dic.keys())) + len(a)
    
