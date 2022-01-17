from itertools import permutations

def solution(inputArray):
    perms = [list(perm) for perm in list(permutations(inputArray))]
    
    for perm in perms:
        checklist = []
        for i in range(len(perm)-1):
        
            boo = check(perm[i], perm[i+1])
            checklist.append(boo)
                
        if all(checklist):
            return True
    
    return False
            
            
            
def check(word1, word2):

    diff = 0
    
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff += 1

    if diff == 1:
        return True
    else:
        return False
            
            
    
    
    
