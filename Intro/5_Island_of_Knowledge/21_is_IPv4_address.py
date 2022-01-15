def solution(inputString):
    li = inputString.split('.')
    
    print(li)
    
    if len(li) != 4:
        return False
    elif '' in li:
        return False
    else:
        for i in range(len(li)):
            if li[i].isnumeric():
                if len(li[i]) != len(str(int(li[i]))):
                    return False
                if li[i].count('0') > 1:
                    return False
                if int(li[i]) < 0 or int(li[i]) > 255:
                    return False
            else:
                return False
        return True