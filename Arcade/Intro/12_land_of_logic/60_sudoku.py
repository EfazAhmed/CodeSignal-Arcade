def solution(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            current = grid[i][j]
            row = grid[i]
            column = getColumn(grid, j)
            
            if row.count(current) > 1 or column.count(current) > 1:
                return False
                
    for i in range(0, len(grid), 3):
        for j in range(0, len(grid[i]), 3):
            sub = subGrid(grid, i, j)
            if checkSubGrid(sub) == False:
                return False
                
    return True
            


def getColumn(grid, j):
    temp = []
    for i in range(len(grid)):
        temp.append(grid[i][j])
    return temp
    
def subGrid(grid, i, j):
    temp = [grid[i][j], grid[i][j+1], grid[i][j+2],
            grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
            grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]]
    print(temp)
    return temp
    
def checkSubGrid(grid):
    if len(grid) == len(set(grid)):
        return True
    return False