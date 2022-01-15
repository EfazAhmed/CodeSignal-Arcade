def solution(code):
    return breakdown(code)

def breakdown(s):
    if len(s) <= 8:
        return transform(s)
    else:
        temp = s[:8]
        s = s[8:]
        return transform(temp) + breakdown(s)
        
def transform(s):
    value = int(s, 2)
    letter = chr(value)
    return letter
    