def solution(inputString):
    temp = ""
    for letter in inputString:
        temp += convert(letter)
    return temp
    
def convert(letter):
    value = ord(letter) + 1
    
    if value == 123:
        return "a"
    else:
        return chr(value)