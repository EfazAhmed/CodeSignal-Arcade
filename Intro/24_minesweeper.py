def solution(matrix):
    arr = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix[0])):
            if matrix[i][j] == True:
                temp.append([True, 0])
            else:
                temp.append([False, 0])
        arr.append(temp)
    

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            
            # Top row
            if i == 0:
                # Top left
                if j == 0:
                    if arr[i][j+1][0] == True:
                        arr[i][j][1] += 1
                    if arr[i+1][j+1][0] == True:
                        arr[i][j][1] += 1
                    if arr[i+1][j][0] == True:
                        arr[i][j][1] += 1
                # Top right
                elif j == len(arr[0])-1:
                    if arr[i][j-1][0] == True:
                        arr[i][j][1] += 1
                    if arr[i+1][j-1][0] == True:
                        arr[i][j][1] += 1
                    if arr[i+1][j][0] == True:
                        arr[i][j][1] += 1
                # Top middle
                elif j > 0 and j < len(arr[0])-1:
                    if arr[i][j-1][0] == True:
                        arr[i][j][1] += 1
                    if arr[i+1][j-1][0] == True:
                        arr[i][j][1] += 1
                    if arr[i+1][j][0] == True:
                        arr[i][j][1] += 1
                    if arr[i+1][j+1][0] == True:
                        arr[i][j][1] += 1
                    if arr[i][j+1][0] == True:
                        arr[i][j][1] += 1
            # Bottom row
            elif i == len(arr)-1:
                # Bottom left
                if j == 0:
                    if arr[i][j+1][0] == True:
                        arr[i][j][1] += 1
                    if arr[i-1][j+1][0] == True:
                        arr[i][j][1] += 1
                    if arr[i-1][j][0] == True:
                        arr[i][j][1] += 1
                # Bottom right
                elif j == len(arr[0])-1:
                    if arr[i][j-1][0] == True:
                        arr[i][j][1] += 1
                    if arr[i-1][j-1][0] == True:
                        arr[i][j][1] += 1
                    if arr[i-1][j][0] == True:
                        arr[i][j][1] += 1
                # Top middle
                elif j > 0 and j < len(arr[0])-1:
                    if arr[i][j-1][0] == True:
                        arr[i][j][1] += 1
                    if arr[i-1][j-1][0] == True:
                        arr[i][j][1] += 1
                    if arr[i-1][j][0] == True:
                        arr[i][j][1] += 1
                    if arr[i-1][j+1][0] == True:
                        arr[i][j][1] += 1
                    if arr[i][j+1][0] == True:
                        arr[i][j][1] += 1
            # Left side
            elif j == 0:
                if arr[i-1][j][0] == True:
                    arr[i][j][1] += 1
                if arr[i-1][j+1][0] == True:
                    arr[i][j][1] += 1
                if arr[i][j+1][0] == True:
                    arr[i][j][1] += 1
                if arr[i+1][j+1][0] == True:
                    arr[i][j][1] += 1
                if arr[i+1][j][0] == True:
                    arr[i][j][1] += 1
            # Right side
            elif j == len(arr[0])-1:
                if arr[i-1][j][0] == True:
                    arr[i][j][1] += 1
                if arr[i-1][j-1][0] == True:
                    arr[i][j][1] += 1
                if arr[i][j-1][0] == True:
                    arr[i][j][1] += 1
                if arr[i+1][j-1][0] == True:
                    arr[i][j][1] += 1
                if arr[i+1][j][0] == True:
                    arr[i][j][1] += 1
            elif i > 0 and i < len(arr)-1 and j > 0 and j < len(arr[0])-1:
                if arr[i-1][j][0] == True:
                    arr[i][j][1] += 1
                if arr[i+1][j][0] == True:
                    arr[i][j][1] += 1
                if arr[i][j-1][0] == True:
                    arr[i][j][1] += 1
                if arr[i][j+1][0] == True:
                    arr[i][j][1] += 1
                if arr[i-1][j-1][0] == True:
                    arr[i][j][1] += 1
                if arr[i+1][j+1][0] == True:
                    arr[i][j][1] += 1
                if arr[i+1][j-1][0] == True:
                    arr[i][j][1] += 1
                if arr[i-1][j+1][0] == True:
                    arr[i][j][1] += 1

                
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] = arr[i][j][1]
  
    return arr
    
    
                
            
                
            
            
    
    