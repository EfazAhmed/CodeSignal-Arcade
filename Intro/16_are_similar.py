from itertools import combinations

def solution(a, b):
    if a == b:
        return True
        
    count = 0
    list1 = []
    list2 = []
    
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
            list1.append(a[i])
            list2.append(b[i])
            print(i)

    return count == 2 and set(list1) == set(list2)
            
