def solution(current, numberOfDigits):
    count = 0
    
    while True:
        count += len(str(current))
        if count > numberOfDigits:
            return current - 1
        elif count == numberOfDigits:
            return current
        else:
            current += 1
        

