def solution(string1, string2):
    return check(string1, string2) and check(string2, string1)
    
    
def check(a,b): 
    dic = {}
    for i in range(len(a)):
        if a[i] not in dic.keys():
            dic[a[i]] = b[i]
        else:
            value = dic[a[i]]
            if value != b[i]:
                return False
                
    return True