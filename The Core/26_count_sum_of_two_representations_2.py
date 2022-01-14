def solution(n, l, r):
    count = 0
    for i in range(l, r+1):
        a = i
        b = n - a
        if a <= b and b >= l and b <= r:
            count += 1        
    return count