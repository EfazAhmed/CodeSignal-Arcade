def solution(deposit, rate, threshold):
    curr = deposit
    count = 0
    while True:
        if curr >= threshold:
            return count
        curr *= (1 + (rate/100))
        count += 1
