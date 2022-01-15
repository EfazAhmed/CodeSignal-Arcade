def solution(l, r):
    dic = {}
    for x in range(l, r+1):
        a = x
        lower = a - sumOfDigits(a)
        higher = a + sumOfDigits(a) + 1
        temp = [x for x in range(lower, higher)]
        temp.remove(a)
        dic[x] = temp
       
    count = 0
     
    for x in range(l, r+1):
        temp = dic[x]
        for key in temp:
            if key in dic.keys():
                if x in dic[key]:
                    count += 1
            
    return count // 2

def sumOfDigits(n):
    return sum([int(x) for x in str(n)])
        
