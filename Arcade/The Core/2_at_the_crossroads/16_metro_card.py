def solution(lastNumberOfDays):
    if lastNumberOfDays == 30:
        return [31]
    elif lastNumberOfDays == 31:
        return [28,30,31]
    else:
        return [31]

