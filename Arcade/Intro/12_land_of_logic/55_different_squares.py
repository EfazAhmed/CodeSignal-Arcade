def solution(matrix):
    height = len(matrix)
    width = len(matrix[0])
    
    if height < 2 or width < 2:
        return 0
    elif height == 2 and width == 2:
        return 1
    
    combos = []
    
    for i in range(height-1):
        for j in range(width-1):
            temp = [[matrix[i][j], matrix[i][j+1]],
                    [matrix[i+1][j], matrix[i+1][j+1]]]
            if temp not in combos:
                combos.append(temp)
                
    return len(combos)
