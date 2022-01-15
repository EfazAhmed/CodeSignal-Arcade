def solution(picture):
    answer = []
    
    length = len(picture[0]) + 2
    
    answer.append("*"*length)
    
    for row in picture:
        answer.append('*' + row + '*')
        
    answer.append("*"*length)
    return answer
