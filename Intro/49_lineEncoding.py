def solution(s):
    li = []
    temp = ""
    for i in range(len(s)):
        temp += s[i]
        if len(set(temp)) > 1:
            temp = temp[:-1]
            li.append(transform(temp))
            temp = s[i]
    li.append(transform(temp))
    return "".join(li)
        
    
def transform(s):
    count = len(s)
    if count > 1:
        new = str(count) + s[0]
        return new
    else: 
        return s
        
