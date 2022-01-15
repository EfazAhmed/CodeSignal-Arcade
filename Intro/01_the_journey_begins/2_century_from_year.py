def solution(year):
    temp = float(year)
    number = temp / 100
    
    if int(number) == number:
        return int(number)
    else:
        return int(number) + 1

