def solution(text):
    
    temp = ""
    for i in range(len(text)):
        if text[i].isalpha() or text[i] == " ":
            temp += text[i]
        else:
            temp += " "
    
    li = temp.split(" ")
    
    max_ = 0
    word = ""
    
    for el in li:
        length = len(el)
        if length > max_:
            max_ = length
            word = el
            
    return word
