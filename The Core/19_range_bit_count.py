def solution(a, b):
    temp = [x for x in range(a, b+1)]
    
    total = 0
    
    for x in temp:
        binary = bin(x)[2:].zfill(8)
        count = binary.count("1")
        total += count
        print(x, binary)
        
    return total
