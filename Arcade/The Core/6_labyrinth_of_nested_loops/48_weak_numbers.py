def solution(n):
    max_value = 0
    count = 0
    dlist = []
    for i in range(1,n+1):
        value = getDivisors(i)
        temp = sorted(dlist, reverse=True)
        t_count = 0
        for i in range(len(temp)):
            if temp[i] > value:
                t_count += 1
            else:
                break
        dlist.append(value)
        
        if t_count > max_value:
            max_value = t_count
            count = 1
        elif t_count == max_value:
            count += 1
    
    return [max_value, count]
        
def getDivisors(n):
    count = 1
    for i in range(1, n+1//2):
        if n % i == 0:
            count += 1
    return count
