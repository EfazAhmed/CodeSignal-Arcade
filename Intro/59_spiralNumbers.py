def solution(n):
    limit = n * n
    array = []
    
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        array.append(temp)
        
    i = 0
    j = 0
    curr = 1
    direction = "right"
    

    while True:
        
        if last(array, i, j):
            array[i][j] = curr
            return array
            
        if direction == "right":
            while True:
                if array[i][j] == 0:
                    
                    #place point
                    array[i][j] = curr
                    curr += 1
                    
                    try:
                        if array[i][j+1] == 0:
                            j += 1
                        else:
                            direction = "down"
                            array[i][j] = 0
                            curr -= 1
                            break
                    except IndexError:
                        direction = "down"
                        array[i][j] = 0
                        curr -= 1
                        break
                else:
                    direction = "down"
                    array[i][j] = 0
                    curr -= 1
                    break
        
      
        if direction == "down":
            while True:
                if array[i][j] == 0:
                    
                    #place point
                    array[i][j] = curr
                    curr += 1

                    try:
                        if array[i+1][j] == 0:
                            i += 1
                        else:
                            direction = "left"
                            array[i][j] = 0
                            curr -= 1
                            break
                    except IndexError:
                        direction = "left"
                        array[i][j] = 0
                        curr -= 1
                        break
                else:
                    direction = "left"
                    array[i][j] = 0
                    curr -= 1
                    break
                    
        if direction == "left":
            while True:
                if array[i][j] == 0:
                    
                    #place point
                    array[i][j] = curr
                    curr += 1
                    
                    try:
                        if array[i][j-1] == 0:
                            j -= 1
                        else:
                            direction = "up"
                            array[i][j] = 0
                            curr -= 1
                            break
                    except IndexError:
                        direction = "up"
                        array[i][j] = 0
                        curr -= 1
                        break
                else:
                    direction = "up"
                    array[i][j] = 0
                    curr -= 1
                    break
                    
        if direction == "up":
            while True:
                if array[i][j] == 0:
                    print(i,j)
                    
                    #place point
                    array[i][j] = curr
                    curr += 1

                    try:
                        if array[i-1][j] == 0:
                            i -= 1
                        else:
                            direction = "right"
                            array[i][j] = 0
                            curr -= 1
                            break
                    except IndexError:
                        direction = "right"
                        array[i][j] = 0
                        curr -= 1
                        break
                else:
                    direction = "right"
                    array[i][j] = 0
                    curr -= 1
                    break
                        

    

def last(array, i, j):
    if array[i][j+1] != 0:
        if array[i][j-1] != 0:
            if array[i+1][j] != 0:
                if array[i-1][j] != 0:
                    return True
    return False
