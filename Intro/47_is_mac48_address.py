def solution(inputString):
    if inputString.count("-") !=5:
        return False
    else:
        divisions = inputString.split("-")
        if len(divisions) != 6:
            return False
        else:
            for div in divisions:
                if len(div) == 2:
                    for char in div:
                        value = ord(char)
                        if value < 48 or (value > 58 and value < 65) or value > 70:
                            return False
                else:
                    return False
        return True
