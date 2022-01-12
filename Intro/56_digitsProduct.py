def solution(product):
    if product == 0: 
        return 10
    for i in range(3600):
        a = 1
        for j in str(i):
            a *= int(j)
        if a == product: 
            return i
    return -1
