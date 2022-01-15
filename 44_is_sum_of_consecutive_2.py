def solution(n):
    
    if n < 3:
        return 0
    
    temp = [x for x in range(1,n)]
    
    pointer1 = 0
    pointer2 = 1
    count = 0
    curr = temp[pointer1] + temp[pointer2]
    
    while True:
        if pointer1 < pointer2:
            if curr == n:
                count += 1
                if pointer2 < len(temp) - 1:
                    pointer2 += 1
                    curr += temp[pointer2]
            elif curr < n:
                if pointer2 < len(temp) - 1:
                    pointer2 += 1
                    curr += temp[pointer2]
            else:
                if pointer1 < len(temp) - 1:
                    curr -= temp[pointer1]
                    pointer1 += 1
        else:
            break
                    
            
    return count