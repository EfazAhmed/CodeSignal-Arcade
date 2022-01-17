def solution(startTag):
    idx = startTag.find(" ")
    
    if idx == -1:
        return startTag[0] + '/' + startTag[1:]
        
    part = startTag[:idx]
    return part[0] + '/' + part[1:] + '>'
