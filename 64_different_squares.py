def solution(matrix):
    li = []
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])-1):
            temp = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]
            if temp not in li:
                li.append(temp)
    return len(li)
