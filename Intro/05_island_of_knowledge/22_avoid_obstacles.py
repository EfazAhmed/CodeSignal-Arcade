def solution(inputArray):
    li = sorted(inputArray)
    
    counter = 0
    add = 2
    
    while True:
        counter += add
        if counter in li:
            counter = 0
            add += 1
        elif counter > max(li):
            break
            
    return add
            
