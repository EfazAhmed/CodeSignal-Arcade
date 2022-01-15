def solution(statues):
    count = 0
    statues.sort()
    
    for i in range(statues[0]+1, statues[-1]):
        if i not in statues:
            count += 1
    
    return count
