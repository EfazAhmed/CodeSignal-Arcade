def solution(param1, param2):
    if len(str(param2)) > len(str(param1)):
        param1 = str(0)*(len(str(param2))-len(str(param1)))+str(param1)
        param2 = str(param2)
    else:
        param2 = str(0)*(len(str(param1))-len(str(param2)))+str(param2)
        param1 = str(param1)
        
    answer = ""
        
    for i in range(len(param1)):
        first = int(param1[i])
        second = int(param2[i])
        total = first + second
        lastDigit = total % 10
        answer += str(lastDigit)

    return int(answer)
    
