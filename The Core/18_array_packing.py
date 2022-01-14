def solution(a):
    temp = ""
    for i in range(len(a)):
        value = bin(a[i])[2:].zfill(8)
        temp = value + temp
        
    if temp != "":
        return int(temp,2)
    return temp
