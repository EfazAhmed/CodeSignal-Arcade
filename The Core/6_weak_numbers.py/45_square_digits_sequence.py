def solution(a0):
    memory = [a0]
    
    while True:
        a0 = transform(a0)
        if a0 in memory:
            memory.append(a0)  
            return len(memory)
        if a0 not in memory:
            memory.append(a0)       
        

def transform(num):
    return sum([int(pow(int(x),2)) for x in str(num)])