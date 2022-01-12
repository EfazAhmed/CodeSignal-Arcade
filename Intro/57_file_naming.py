def solution(names):
    freq = {}
    
    org = names.copy()
    
    for i in range(1, len(names)):
        count = names[:i].count(names[i])
        if count > 0:
            temp = names[i] + f"({count})"
            while temp in names[:i]:
                temp = names[i] + f"({count})"
                count += 1 
            names[i] = temp
    return names
